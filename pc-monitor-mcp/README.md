# PC Monitor MCP Server

A local, read-only MCP (Model Context Protocol) server that lets Claude Code
view basic stats about your computer — CPU, RAM, disk, and GPU usage.

## What this does

This runs as a small local process that Claude Code starts and talks to
over stdin/stdout only (no network port, no listening service). It exposes
four tools:

- `cpu_usage` — current CPU usage percentage
- `ram_usage` — total / used / available RAM (GB) and usage percentage
- `disk_usage` — total / used / free space (GB) and usage percentage for the `C:\` drive
- `gpu_usage` — NVIDIA GPU name, usage percentage, temperature, and memory usage (returns "not available" on non-NVIDIA systems)

**What it does NOT do:** it cannot write, delete, move, or execute anything
on your system, does not require administrator privileges, and makes no
outbound network calls of its own. See the "Security" section below.

## Installation

1. Make sure Python 3.10+ is installed (`py --version`).
2. From this folder, create a virtual environment and install dependencies:

   ```
   py -m venv venv
   venv\Scripts\pip install -r requirements.txt
   ```

## Running it directly (for testing)

```
venv\Scripts\python -m pc_monitor_mcp.server
```

It will sit waiting for MCP messages on stdin — that's expected, it's
designed to be launched by an MCP client (like Claude Code), not run
interactively. Press Ctrl+C to stop it.

## Connecting it to Claude Code

From anywhere, run:

```
claude mcp add pc-monitor -e PYTHONPATH="C:\Users\ryans\practise\pc-monitor-mcp\src" -- "C:\Users\ryans\practise\pc-monitor-mcp\venv\Scripts\python.exe" -m pc_monitor_mcp.server
```

This registers the server using the venv's own Python interpreter, so it
always has access to the packages installed in `requirements.txt`. The
`PYTHONPATH` environment variable is required so that `pc_monitor_mcp` is
importable regardless of what directory Claude Code launches it from.

Then verify it connected:

```
/mcp
```

You should see `pc-monitor` listed as connected, with the four tools
(`cpu_usage`, `ram_usage`, `disk_usage`, `gpu_usage`) available.

## Testing

Run the test suite:

```
venv\Scripts\pip install pytest
venv\Scripts\pytest tests/
```

To test each tool manually, you can also just call the underlying
functions directly in a Python shell:

```
venv\Scripts\python
>>> from pc_monitor_mcp.monitors import get_cpu_usage, get_ram_usage, get_disk_usage, get_gpu_usage
>>> get_cpu_usage()
>>> get_ram_usage()
>>> get_disk_usage()
>>> get_gpu_usage()
```

Each function should return a plain dictionary of numbers — no exceptions,
even if (for `get_gpu_usage`) no NVIDIA GPU is present.

## Security

- **Local only** — communicates with Claude Code exclusively via stdio (stdin/stdout of a local subprocess). No network port is opened.
- **No admin privileges required** — all four tools read OS-exposed counters via `psutil` and `pynvml`, both of which work as a normal user on Windows.
- **Read-only** — there is no file-write, delete, move, or command-execution capability anywhere in this codebase. The only actions available are the four monitoring functions in `monitors.py`.
- **No outbound network calls** — this server itself never makes an HTTP request or contacts any external service. (Note: the *results* returned by these tools do become part of your conversation with Claude, and are sent to Anthropic's API as part of normal Claude Code operation — that's true of any MCP tool, not specific to this one.)
- **No personal data collected or stored** — nothing is written to disk by this server; every tool call reads live system counters and returns them, nothing is logged or persisted.

## Safely expanding this project later

If you want to add more tools in future (e.g. per-process CPU usage, network
I/O stats, battery status), keep to the same pattern:

1. Add a new read-only function to `monitors.py`.
2. Register it as a tool in `server.py`.
3. Add a test in `tests/test_monitors.py`.

Avoid adding anything that writes to disk, executes external commands, or
opens a network listener — those would break the security guarantees this
project was built around. If a future feature genuinely needs elevated
permissions (e.g. some hardware sensors require admin access), treat that
as a deliberate, separately-approved decision, not a default.
