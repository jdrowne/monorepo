import pytest


# 1.1.2 Ensure separate partition exists for /tmp
def test_cis_benchmark_1_1_2(host):
  assert host.mount_point('/tmp').exists
