import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_available(host):
    assert host.package('nginx').is_installed
    assert host.service('nginx').is_running
    assert host.service('nginx').is_enabled


def test_docroot_index(host):
    f = host.file('/var/www/html/index.html')
    assert f.exists
    assert f.mode == 0o644

    cmd = host.run("grep 'DevOps TO' /var/www/html/index.html")
    assert cmd.rc == 0
