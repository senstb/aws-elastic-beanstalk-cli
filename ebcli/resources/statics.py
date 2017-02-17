# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

# TODO: Merge into ebcli/lib/iam_role.py when the code has been merged in
class iam_documents(object):
    EC2_ASSUME_ROLE_PERMISSION = '{"Version": "2008-10-17","Statement": [{"Action":' \
            ' "sts:AssumeRole","Principal": {"Service": ' \
            '"ec2.amazonaws.com"},"Effect": "Allow","Sid": ""}]}'
    CUSTOM_PLATFORM_BUILDER_INLINE_POLICY = '{"Version":"2012-10-17","Statement":[{"Effect":' \
                                            '"Allow","Action":["ec2:AttachVolume","ec2:AuthorizeSecurityGroupIngress",' \
                                            '"ec2:CopyImage","ec2:CreateImage","ec2:CreateKeypair",' \
                                            '"ec2:CreateSecurityGroup","ec2:CreateSnapshot","ec2:CreateTags",' \
                                            '"ec2:CreateVolume","ec2:DeleteKeypair","ec2:DeleteSecurityGroup",' \
                                            '"ec2:DeleteSnapshot","ec2:DeleteVolume","ec2:DeregisterImage",' \
                                            '"ec2:DescribeImageAttribute","ec2:DescribeImages","ec2:DescribeInstances",' \
                                            '"ec2:DescribeRegions","ec2:DescribeSecurityGroups","ec2:DescribeSnapshots",' \
                                            '"ec2:DescribeSubnets","ec2:DescribeTags","ec2:DescribeVolumes",' \
                                            '"ec2:DetachVolume","ec2:GetPasswordData","ec2:ModifyImageAttribute",' \
                                            '"ec2:ModifyInstanceAttribute","ec2:ModifySnapshotAttribute",' \
                                            '"ec2:RegisterImage","ec2:RunInstances","ec2:StopInstances",' \
                                            '"ec2:TerminateInstances"],"Resource":"*"}]}'

class iam_attributes(object):
    DEFAULT_PLATFORM_BUILDER_ROLE = 'aws-elasticbeanstalk-custom-platform-ec2-role'
    PLATFORM_BUILDER_INLINE_POLICY_NAME = 'EB_Custom_Platform_Builder_Policy'


class namespaces(object):
    AUTOSCALING = 'aws:autoscaling:asg'
    COMMAND = 'aws:elasticbeanstalk:command'
    RDS = 'aws:rds:dbinstance'
    ENVIRONMENT = 'aws:elasticbeanstalk:environment'
    HEALTH_CHECK = 'aws:elb:healthcheck'
    HEALTH_SYSTEM = 'aws:elasticbeanstalk:healthreporting:system'
    LAUNCH_CONFIGURATION = 'aws:autoscaling:launchconfiguration'
    LOAD_BALANCER = 'aws:elb:loadbalancer'
    ELB_POLICIES = 'aws:elb:policies'
    ROLLING_UPDATES = 'aws:autoscaling:updatepolicy:rollingupdate'
    VPC = 'aws:ec2:vpc'
    CLOUDWATCH_LOGS = 'aws:elasticbeanstalk:cloudwatch:logs'


class option_names(object):
    BATCH_SIZE = 'BatchSize'
    BATCH_SIZE_TYPE = 'BatchSizeType'
    CONNECTION_DRAINING = 'ConnectionDrainingEnabled'
    CROSS_ZONE = 'CrossZone'
    DB_DELETION_POLICY = 'DBDeletionPolicy'
    DB_ENGINE = 'DBEngine'
    DB_ENGINE_VERSION = 'DBEngineVersion'
    DB_INSTANCE = 'DBInstanceClass'
    DB_PASSWORD = 'DBPassword'
    DB_STORAGE_SIZE = 'DBAllocatedStorage'
    DB_SUBNETS = 'DBSubnets'
    DB_USER = 'DBUser'
    EC2_KEY_NAME = 'EC2KeyName'
    ELB_SCHEME = 'ELBScheme'
    ELB_SUBNETS = 'ELBSubnets'
    ENVIRONMENT_TYPE = 'EnvironmentType'
    IAM_INSTANCE_PROFILE = 'IamInstanceProfile'
    INSTANCE_TYPE = 'InstanceType'
    INTERVAL = 'Interval'
    LOAD_BALANCER_HTTP_PORT = 'LoadBalancerHTTPPort'
    LOAD_BALANCER_HTTPS_PORT = 'LoadBalancerHTTPSPort'
    LOAD_BALANCER_TYPE = 'LoadBalancerType'
    MAX_SIZE = 'MaxSize'
    MIN_SIZE = 'MinSize'
    PUBLIC_IP = 'AssociatePublicIpAddress'
    ROLLING_UPDATE_ENABLED = 'RollingUpdateEnabled'
    ROLLING_UPDATE_TYPE = 'RollingUpdateType'
    SECURITY_GROUPS = 'SecurityGroups'
    SERVICE_ROLE = 'ServiceRole'
    SUBNETS = 'Subnets'
    SSL_CERT_ID = 'SSLCertificateId'
    SYSTEM_TYPE = 'SystemType'
    VPC_ID = 'VPCId'
    STREAM_LOGS = 'StreamLogs'
    DELETE_ON_TERMINATE = 'DeleteOnTerminate'
    RETENTION_DAYS = 'RetentionInDays'


class elb_names(object):
    HEALTHY_STATE = 'healthy'
    UNHEALTHY_STATE = 'unhealthy'
    V2_RESOURCE_TYPE = 'AWS::ElasticLoadBalancingV2::TargetGroup'
    DEFAULT_PROCESS_LOGICAL_ID = 'AWSEBV2LoadBalancerTargetGroup'
    CLASSIC_VERSION = 'classic'
    APPLICATION_VERSION = 'application'
