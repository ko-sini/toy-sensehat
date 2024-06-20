# Infra

## Terraform

`-chdir` or `cd` to infra directory and initialize.
```bash
terraform -chdir="./s3" init
```

Plan
```bash
terraform -chdir="./s3" plan
```

Remember to run terraform format every now and then, and especially before pushing code!
```bash
terraform -chdir="./s3" fmt
```

Apply planned changes
```bash
terraform -chdir="./s3" apply
```


## Installation

- Install terraform CLI, see https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
- Install AWS CLI v2 from source
    ```bash
    git clone git@github.com:aws/aws-cli.git
    cd aws-cli
    git checkout v2
    pip3 install -r requirements.txt --upgrade --user 
    pip3 install . --upgrade --user 
    export PATH=/home/<user>/.local/bin:$PATH
    ```
- Confirm installation by e.g. running `aws --version`
- Add credentials by copying `provider.env` to `.env` and inserting required keys. Session token is not needed.
    ```bash
    export AWS_ACCESS_KEY_ID=""
    export AWS_SECRET_ACCESS_KEY=""
    export AWS_SESSION_TOKEN=""
    ```
- Make sure you have the environment variables defined by running `source .env`