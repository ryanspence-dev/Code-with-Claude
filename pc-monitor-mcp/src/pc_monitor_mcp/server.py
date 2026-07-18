"""MCP server exposing read-only PC monitoring tools over stdio.

Run with:  python -m pc_monitor_mcp.server

This process only talks to Claude Code over stdin/stdout (the MCP stdio
transport). It does not open any network port and does not make any
outbound network calls itself.
"""

from mcp.server.fastmcp import FastMCP

from pc_monitor_mcp.monitors import (
    CpuUsage,
    DiskUsage,
    GpuUsage,
    RamUsage,
    get_cpu_usage,
    get_disk_usage,
    get_gpu_usage,
    get_ram_usage,
)

mcp = FastMCP("pc-monitor")


@mcp.tool()
def cpu_usage() -> CpuUsage:
    """Get current CPU usage percentage."""
    return get_cpu_usage()


@mcp.tool()
def ram_usage() -> RamUsage:
    """Get RAM usage: total, used, available (GB) and usage percentage."""
    return get_ram_usage()


@mcp.tool()
def disk_usage() -> DiskUsage:
    """Get storage usage for the main drive (C:\\): total, used, free (GB) and usage percentage."""
    return get_disk_usage()


@mcp.tool()
def gpu_usage() -> GpuUsage:
    """Get NVIDIA GPU info if available: name, usage percentage, temperature, memory usage."""
    return get_gpu_usage()


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
