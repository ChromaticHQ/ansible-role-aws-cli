import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_aws_dir(host):
    f = host.file('/var/lib/jenkins/.aws')

    assert f.exists
    assert f.is_directory
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'


def test_aws_config_file(host):
    f = host.file('/var/lib/jenkins/.aws/config')

    assert f.exists
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'
    assert f.contains('region=us-east-1')
    assert f.contains('output=json')


def test_aws_credentials_file(host):
    f = host.file('/var/lib/jenkins/.aws/credentials')

    assert f.exists
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'
    assert f.contains('aws_access_key_id=molecule-aws-access-key-id')
    assert f.contains('aws_secret_access_key=molecule-aws-secret-access-key')
