import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users(host):
    assert host.user('newrelic').group == 'newrelic'


def test_packages(host):
    packages = [
        'newrelic-daemon', 'newrelic-infra', 'newrelic-php5',
        'newrelic-php5-common',
    ]
    for package in packages:
        assert host.package(package).is_installed


def test_config(host):
    php_ini = host.file('/etc/php/7.0/mods-available/newrelic.ini')
    assert 'newrelic.daemon.loglevel = error' in php_ini.content_string
