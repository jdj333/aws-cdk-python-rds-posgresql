# AWS CDK RDS PostgreSQL Project

This project contains an AWS CDK stack that deploys an RDS PostgreSQL database. The deployment is automated using GitHub Actions.

## Project Structure

```
cdk_project/
├── app.py
├── requirements.txt
└── .github/
    └── workflows/
        └── deploy.yml
```

## Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured.
- [Node.js](https://nodejs.org/) (for AWS CDK) installed.
- [Python 3.9](https://www.python.org/downloads/) installed.
- [AWS CDK](https://aws.amazon.com/cdk/) installed globally.

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/jdj333/aws-cdk-python-rds-postgresql.git
    cd aws-cdk-python-rds-postgresql/cdk_project
    ```

2. **Install dependencies:**

    ```sh
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    npm install -g aws-cdk
    ```

3. **Bootstrap your environment (if not already done):**

    ```sh
    cdk bootstrap aws://ACCOUNT-NUMBER/REGION
    ```

## CDK Commands

1. **Synthesize the CloudFormation template:**

    ```sh
    cdk synth
    ```

2. **Deploy the stack:**

    ```sh
    cdk deploy
    ```

3. **Destroy the stack:**

    ```sh
    cdk destroy
    ```

4. **Check the diff between deployed stack and local changes:**

    ```sh
    cdk diff
    ```

## GitHub Actions Deployment

This project includes a GitHub Actions workflow for automatic deployment.

**Relative Path: `.github/workflows/deploy.yml`**

```yaml
name: Deploy RDS PostgreSQL Database

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          npm install -g aws-cdk

      - name: CDK Deploy
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: 'us-west-2'
        run: cdk deploy --require-approval never
```

## Setting Up GitHub Secrets

Ensure you have the following secrets set up in your GitHub repository:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Useful Links

- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [AWS RDS Documentation](https://docs.aws.amazon.com/rds/index.html)
- [Secrets Manager Documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

