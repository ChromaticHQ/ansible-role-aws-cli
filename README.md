[![Build
Status](https://travis-ci.org/ChromaticHQ/ansible-role-aws-cli.svg?branch=master)](https://travis-ci.org/ChromaticHQ/ansible-role-aws-cli)

# AWS CLI

This role:

1. Uses PIP to perform a basic install of [Amazon's AWS CLI tools](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), and
2. Templates [a `config` file and a `credentials` file](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-config-files) into a configurable location for each of a list of one or more users.

## Requirements

No special requirements.

## Role Variables

- `aws_users` (default `[]`): a list of aws users to configure once aws cli is
  installed.

  ```yaml
  # Example `aws_users` configuration.
  aws_users:
    - name: jenkins,
      group: jenkins,
      region: us-east-1
      output: json
      home: /var/lib
  ```

- `aws_cli_config` (default `config.js`): the filename or path to the template file used to
  create `~/.aws/config`.

- `aws_cli_credentials` (default `credentials.js`): the filename or path to the template file
  used to create `~/.aws/credentials`.

## Dependencies

No special dependencies.
