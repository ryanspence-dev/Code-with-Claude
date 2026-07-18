"""Tests for the read-only monitoring functions.

These call the plain functions directly (no MCP protocol involved) and
check the shape and sanity of the values returned.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from pc_monitor_mcp.monitors import (  # noqa: E402
    get_cpu_usage,
    get_disk_usage,
    get_gpu_usage,
    get_ram_usage,
)


def test_get_cpu_usage_returns_valid_percentage():
    result = get_cpu_usage()
    assert 0.0 <= result["usage_percent"] <= 100.0


def test_get_ram_usage_returns_consistent_values():
    result = get_ram_usage()
    assert result["total_gb"] > 0
    assert result["used_gb"] >= 0
    assert result["available_gb"] >= 0
    assert 0.0 <= result["usage_percent"] <= 100.0
    # used should never exceed total
    assert result["used_gb"] <= result["total_gb"]


def test_get_disk_usage_returns_consistent_values():
    result = get_disk_usage()
    assert result["drive"] == "C:\\"
    assert result["total_gb"] > 0
    assert result["used_gb"] >= 0
    assert result["free_gb"] >= 0
    assert 0.0 <= result["usage_percent"] <= 100.0


def test_get_gpu_usage_never_raises_and_has_expected_shape():
    result = get_gpu_usage()
    assert "available" in result
    if result["available"]:
        assert result["name"]
        assert 0.0 <= result["usage_percent"] <= 100.0
        assert result["memory_used_gb"] <= result["memory_total_gb"]
    else:
        assert result["message"]
