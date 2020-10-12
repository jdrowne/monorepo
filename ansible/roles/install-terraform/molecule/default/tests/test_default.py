import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

HASH = '90a6b8e3772a7e5c5606c84ffc6dfe048202a212525b74cd68bf4e7d4ccab322'
TERRAFORM_BINARY_PATH = '/usr/local/bin/terraform'


def test_terraform_binary_exists(host):
    host.file.exists(TERRAFORM_BINARY_PATH)


def test_terraform_binary_is_a_file(host):
    host.file.is_file(TERRAFORM_BINARY_PATH)


def test_terraform_binary_has_correct_permissions(host):
    host.file(TERRAFORM_BINARY_PATH).mode == 0o755


def test_terraform_binary_has_correct_owner(host):
    host.file(TERRAFORM_BINARY_PATH).user == 'root'


def test_terraform_binary_has_correct_group(host):
    host.file(TERRAFORM_BINARY_PATH).group == 'root'


def test_terraform_runs_from_binary(host):
    host.check_output('which terraform') == TERRAFORM_BINARY_PATH


def test_terraform_binary_is_correct_file(host):
    host.file(TERRAFORM_BINARY_PATH).sha256sum == HASH


def test_terraform_runs_correctly(host):
    host.run_expect([0], 'terraform --version')
