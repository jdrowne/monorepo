"""Role testing files using testinfra."""


def test_libreswan_is_installed(host):
    host.package('libreswan').is_installed


def test_network_manager_is_installed(host):
    host.package('NetworkManager').is_installed


def test_quagga_is_installed(host):
    host.package('quagga').is_installed


def test_ipsec_is_running(host):
    host.service('ipsec').is_running


def test_ipsec_is_enabled(host):
    host.service('ipsec').is_enabled
