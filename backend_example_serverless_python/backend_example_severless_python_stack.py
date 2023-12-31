from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from . import my_handler

class BackendExampleServerlessPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_handler.MyService(self, "MyService")

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "BackendExampleServerlessPythonQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
