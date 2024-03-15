from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk.aws_lambda as _lambda

class ApigwLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a lambda function for get method
        # The code will be automatically uploaded to Lambda by the CDK
        get_lambda = _lambda.Function(self, "get_lambda",
                                      function_name="get_method_lambda",
                                      runtime=_lambda.Runtime.PYTHON_3_12,
                                      code=_lambda.Code.from_asset("lambda"),
                                      handler="get_method.lambda_handler"
                                      )
        
        # create a lambda function for post method
        # You have to pass the value of the body to the lambda function, such as: key=value or {"key": "value"} pair
        post_lambda = _lambda.Function(self, "post_lambda",
                                      function_name="post_method_lambda",
                                      runtime=_lambda.Runtime.PYTHON_3_12,
                                      code=_lambda.Code.from_asset("lambda"),
                                      handler="post_method.lambda_handler"
                                      )