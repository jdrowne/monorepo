import base64, pytest

MODPROBE_CIS_CONF = "/etc/modprobe.d/CIS.conf"


# 1.1.1.1 Ensure mounting of cramfs filesystems is disabled
def test_cis_benchmark_1_1_1_1a(host):
  assert 'install /bin/true' in host.check_output('modprobe -n -v cramfs')


# 1.1.1.1 Ensure mounting of cramfs filesystems is disabled
def test_cis_benchmark_1_1_1_1b(host):
  assert host.run_expect([1], 'lsmod | grep cramfs')


# 1.1.1.2 Ensure mounting of freevxfs filesystems is disabled
def test_cis_benchmark_1_1_1_2a(host):
  assert 'install /bin/true' in host.check_output('modprobe -n -v freevxfs')


# 1.1.1.2 Ensure mounting of freevxfs filesystems is disabled
def test_cis_benchmark_1_1_1_2b(host):
  assert host.run_expect([1], 'lsmod | grep freevxfs')


# 1.1.1.3 Ensure mounting of jffs2 filesystems is disabled
def test_cis_benchmark_1_1_1_3a(host):
  assert 'install /bin/true' in host.check_output('modprobe -n -v jffs2')


# 1.1.1.3 Ensure mounting of jffs2 filesystems is disabled
def test_cis_benchmark_1_1_1_3b(host):
  assert host.run_expect([1], 'lsmod | grep jffs2')


# 1.1.1.4 Ensure mounting of hfs filesystems is disabled
def test_cis_benchmark_1_1_1_4a(host):
  assert 'install /bin/true' in host.check_output('modprobe -n -v hfs')


# 1.1.1.4 Ensure mounting of hfs filesystems is disabled
def test_cis_benchmark_1_1_1_4b(host):
  assert host.run_expect([1], 'lsmod | grep hfs')


# 1.1.1.5 Ensure mounting of hfsplus filesystems is disabled
def test_cis_benchmark_1_1_1_5a(host):
  assert 'install /bin/true' in host.check_output('modprobe -n -v hfsplus')


# 1.1.1.5 Ensure mounting of hfsplus filesystems is disabled
def test_cis_benchmark_1_1_1_5b(host):
  assert host.run_expect([1], 'lsmod | grep hfsplus')


# 1.1.1.6 Ensure mounting of squashfs filesystems is disabled
def test_cis_benchmark_1_1_1_6a(host):
  assert(
    'install /bin/true' in host.check_output('modprobe -n -v squashfs') or
    host.run_expect([0], "grep \"^install squashfs /bin/true\" {}".format(MODPROBE_CIS_CONF))
  )


# 1.1.1.6 Ensure mounting of squashfs filesystems is disabled
def test_cis_benchmark_1_1_1_6b(host):
  assert host.run_expect([1], 'lsmod | grep squashfs')


# 1.1.1.7 Ensure mounting of udf filesystems is disabled
def test_cis_benchmark_1_1_1_7a(host):
  assert 'install /bin/true' in host.check_output('modprobe -n -v udf')


# 1.1.1.7 Ensure mounting of udf filesystems is disabled
def test_cis_benchmark_1_1_1_7b(host):
  assert host.run_expect([1], 'lsmod | grep udf')


# 1.1.1.8 Ensure mounting of vfat filesystems is disabled
def test_cis_benchmark_1_1_1_8a(host):
  assert(
    'install /bin/true' in host.check_output('modprobe -n -v vfat') or
    host.run_expect([0], "grep \"^install vfat /bin/true\" {}".format(MODPROBE_CIS_CONF))
  )


# 1.1.1.8 Ensure mounting of vfat filesystems is disabled
def test_cis_benchmark_1_1_1_8b(host):
  assert host.run_expect([1], 'lsmod | grep vfat')
