#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import aws_rds as rds
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_secretsmanager as secretsmanager

class RdsDatabaseStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define a VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

        # Define the database credentials
        db_credentials = secretsmanager.Secret(self, "DBCredentialsSecret",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template='{"username":"admin"}',
                generate_string_key="password",
                exclude_characters='/@"\''
            )
        )

        # Define the RDS PostgreSQL instance
        db_instance = rds.DatabaseInstance(self, "MyRdsInstance",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_13_3
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            credentials=rds.Credentials.from_secret(db_credentials),
            multi_az=False,
            allocated_storage=20,
            max_allocated_storage=100,
            allow_major_version_upgrade=False,
            auto_minor_version_upgrade=True,
            backup_retention=cdk.Duration.days(7),
            delete_automated_backups=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            deletion_protection=False,
            database_name="mydatabase",
            publicly_accessible=True
        )

app = cdk.App()
RdsDatabaseStack(app, "RdsDatabaseStack")
app.synth()
