# AWS CLI

This role uses PIP to perform a basic install of [Amazon's AWS CLI
tools](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html),
then creates [a `config` file (by `template`), and a credentials file (by
`copy`)](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-config-files)
for each of a list of users.

## Requirements

No special requirements.

## Role Variables

- `aws_users`: a list of aws users to configure once aws cli is
  installed.

  ```yaml
  # Example `aws_users` configuration.
  aws_users:
  - {
    name: jenkins,
    group: jenkins,
    region: us-east-1
    output: json
  }
  ```

## Dependencies

No special dependencies.
