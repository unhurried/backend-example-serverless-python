import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_)

class MyService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        layer = lambda_.LayerVersion(
                self, "MyLayer",
                code=lambda_.Code.from_asset("lambda_layer"),
                compatible_runtimes=[lambda_.Runtime.PYTHON_3_13])

        handler = lambda_.Function(
                self, "MyHandler",
                runtime=lambda_.Runtime.PYTHON_3_13,
                code=lambda_.Code.from_asset("resources"),
                handler="handler.handler",
                layers=[layer])

        api = apigateway.RestApi(self, "my-api",
                  rest_api_name="My Service",
                  description="This service serves apis.")

        get_api_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_api_integration)   # GET /