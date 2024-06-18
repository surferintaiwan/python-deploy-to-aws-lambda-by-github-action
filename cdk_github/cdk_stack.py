import os
import aws_cdk as cdk
import aws_cdk.aws_lambda as lambda_function
from constructs import Construct
ENV = os.getenv('ENV', 'DEV')


class CdkGitHubStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #example resource
        # queue = cdk.sqs.Queue(
        #      self, "CdkGitHubQueue",
        #      visibility_timeout=cdk.Duration.seconds(300),
        # )

        # bucket = cdk.s3.Bucket(self, "MyfirstBucket", versioned=True,
        #                    bucket_name="demo-bucket-beyond-the-cloud-98979867",
        #                    block_public_access=s3.BlockPublicAccess.BLOCK_ALL)

        function = lambda_function.Function(self, f"{ENV}-Test-Function",
                                            function_name=f"{ENV}-Test-Function-Call",
                                            runtime=lambda_function.Runtime.PYTHON_3_9,
                                            code=lambda_function.Code.from_asset('./src'),
                                            handler="index.lambda_handler")
        # set lambda function url
        function_url = function.add_function_url(
            auth_type=lambda_function.FunctionUrlAuthType.NONE
        )

        cdk.CfnOutput(self, "FunctionUrl", value=function_url.url)

        
        