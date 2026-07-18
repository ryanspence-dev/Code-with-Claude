"""Read-only system monitoring functions.

Every function here only reads OS-exposed counters (via psutil / pynvml).
None of them write, delete, move, or execute anything, and none require
administrator privileges on Windows, macOS, or Linux.
"""

from __future__ import annotations

import shutil
from typing import TypedDict

import psutil

try:
    import pynvml

    _NVML_AVAILABLE = True
except ImportError:
    _NVML_AVAILABLE = False


class CpuUsage(TypedDict):
    usage_percent: float


class RamUsage(TypedDict):
    total_gb: float
    used_gb: float
    available_gb: float
    usage_percent: float


class DiskUsage(TypedDict):
    drive: str
    total_gb: float
    used_gb: float
    free_gb: float
    usage_percent: float


class GpuUsage(TypedDict):
    available: bool
    name: str | None
    usage_percent: float | None
    temperature_c: float | None
    memory_used_gb: float | None
    memory_total_gb: float | None
    message: str | None


_BYTES_PER_GB = 1024**3


def get_cpu_usage() -> CpuUsage:
    """Return current system-wide CPU usage as a percentage.

    Blocks for ~0.5s to sample usage over an interval, which is far more
    accurate than an instantaneous reading.
    """
    return {"usage_percent": psutil.cpu_percent(interval=0.5)}


def get_ram_usage() -> RamUsage:
    """Return total, used, available RAM and usage percentage, in GB."""
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total / _BYTES_PER_GB, 2),
        "used_gb": round(mem.used / _BYTES_PER_GB, 2),
        "available_gb": round(mem.available / _BYTES_PER_GB, 2),
        "usage_percent": mem.percent,
    }


def get_disk_usage(drive: str = "C:\\") -> DiskUsage:
    """Return total, used, free space and usage percentage for a drive.

    Defaults to C:\\, the main drive on most Windows machines.
    """
    usage = shutil.disk_usage(drive)
    return {
        "drive": drive,
        "total_gb": round(usage.total / _BYTES_PER_GB, 2),
        "used_gb": round(usage.used / _BYTES_PER_GB, 2),
        "free_gb": round(usage.free / _BYTES_PER_GB, 2),
        "usage_percent": round((usage.used / usage.total) * 100, 1),
    }


def get_gpu_usage() -> GpuUsage:
    """Return NVIDIA GPU name, usage, temperature, and memory if available.

    Uses NVML (via pynvml), which does not require administrator privileges.
    Only NVIDIA GPUs are supported; anything else returns available=False
    with an explanatory message rather than raising an error.
    """
    empty: GpuUsage = {
        "available": False,
        "name": None,
        "usage_percent": None,
        "temperature_c": None,
        "memory_used_gb": None,
        "memory_total_gb": None,
        "message": None,
    }

    if not _NVML_AVAILABLE:
        return {**empty, "message": "pynvml is not installed"}

    try:
        pynvml.nvmlInit()
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            name = pynvml.nvmlDeviceGetName(handle)
            if isinstance(name, bytes):
                name = name.decode()
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            temperature = pynvml.nvmlDeviceGetTemperature(
                handle, pynvml.NVML_TEMPERATURE_GPU
            )
            memory = pynvml.nvmlDeviceGetMemoryInfo(handle)

            return {
                "available": True,
                "name": name,
                "usage_percent": float(utilization.gpu),
                "temperature_c": float(temperature),
                "memory_used_gb": round(memory.used / _BYTES_PER_GB, 2),
                "memory_total_gb": round(memory.total / _BYTES_PER_GB, 2),
                "message": None,
            }
        finally:
            pynvml.nvmlShutdown()
    except pynvml.NVMLError as exc:
        return {**empty, "message": f"No NVIDIA GPU detected ({exc})"}
