[![Build
Status](https://travis-ci.org/ChromaticHQ/ansible-role-aws-cli.svg?branch=master)](https://travis-ci.org/ChromaticHQ/ansible-role-aws-cli)

# AWS CLI

This role:

1. Uses PIP to perform a basic install of [Amazon's AWS CLI tools](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), and
2. Templates [a `config` file and a `credentials` file](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-config-files) into a configurable location for each of a list of one or more users.

## Requirements

No special requirements.

## Role Variables

| Variable Name | Default | Use |
|---------------|---------|-----|
| `aws_users` | `[]` | A list of aws users to configure once `aws-cli` is installed. |
| `aws_users` > `name` | `-` | Each item in `aws_users` should include the `name` of a user to configure `aws-cli` for. |
| `aws_users` > `group` | `-` | Each item in `aws_users` should include the `group` of the user to configure `aws-cli` for. |
| `aws_users` > `region` | `-` | Each item in `aws_users` should include the aws region to add to the `config` file for the user. |
| `aws_users` > `output` | `-` | Each item in `aws_users` should include the `output` format for the `config` file for the user. |
| `aws_users` > `home` | `-` | Eacy item in `aws_users` should include the path to the `home` directory containing the users' home directory. |
| `aws_config` | `config.j2` | The template file used to create the `config` file in the `.aws` directory. |
| `aws_credentials` | `credentials.j2` | The template file used to create the `credentials` file in the `.aws` directory. |
| `aws_access_key_id` | `""` | The aws access key id used to access an aws account. |
| `aws_secret_access_key` | `""` | The secret access key use to access an aws account. |

### Example `aws_users` configuration

  ```yaml
  # Example `aws_users` configuration.
  aws_users:
    - name: jenkins,
      group: jenkins,
      region: us-east-1
      output: json
      home: /var/lib
  ```

## Dependencies

No special dependencies.
