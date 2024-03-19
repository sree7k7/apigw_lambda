from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_apigateway as apigw
import aws_cdk.aws_apigatewayv2 as apigw2
# from aws_cdk import aws_apigatewayv2_integrations as apigw2_integrations
# from aws_cdk.aws_apigatewayv2_integrations import HttpUrlIntegration, HttpLambdaIntegration
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration, HttpUrlIntegration
from aws_cdk.aws_apigatewayv2_authorizers import HttpLambdaAuthorizer
from aws_cdk.aws_apigatewayv2_authorizers import HttpIamAuthorizer



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
        
        #3. Create an API Gateway
        #3.1 Create a REST API
        
        apigwGetPost = apigw2.HttpApi(self, "api_gateway",
                              api_name="APIGw_get_post",
                              description="This is a test API Gateway for GET and POST methods using api keys"
                            )
        # # add stage
        apigwGetPost.add_stage = apigw2.HttpStage(
            self, "api_gateway_stage",
            http_api=apigwGetPost,
            stage_name="testStage",
            auto_deploy=True,  
        )
        
        get_lambda_integration = HttpLambdaIntegration("GetLambdaIntegration", handler=get_lambda)
        apigwGetPost.add_routes(
            path="/get",
            methods=[apigw2.HttpMethod.GET],
            integration=get_lambda_integration
        )

        post_lambda_integration = HttpLambdaIntegration("PostLambdaIntegration", handler=post_lambda)
        apigwGetPost.add_routes(
            path="/post",
            methods=[apigw2.HttpMethod.POST],
            integration=post_lambda_integration
        )

#    books_integration = HttpLambdaIntegration("BooksIntegration", books_default_fn)

#     http_api = apigwv2.HttpApi(self, "HttpApi")

#     http_api.add_routes(
#         path="/books",
#         methods=[apigwv2.HttpMethod.GET],
#         integration=books_integration
#     )
        # lambda_integration = HttpLambdaIntegration("BooksIntegration", handler=get_lambda)
        # # # add Get and Post methods to the API Gateway
        # apigwGetPost.add_routes(
        #     path="/get",
        #     methods=[apigw2.HttpMethod.GET],
        #     integration=lambda_integration
        # )
        # apigwGetPost.root.add_method("POST", apigw2.LambdaIntegration(post_lambda))

        # create usage plan
        # plan = apigw.("UsagePlan",
        #     name="Easy",
        #     throttle=apigw2.ThrottleSettings(
        #         rate_limit=10,
        #         burst_limit=2
        #     )
        # )

        # key = api.add_api_key("ApiKey")
        # plan.add_api_key(key)
        # To associate a plan to a given RestAPI stage:

        # # plan: apigateway.UsagePlan
        # # api: apigateway.RestApi
        # # echo_method: apigateway.Method

        # plan.add_api_stage(
        #     stage=api.deployment_stage,
        #     throttle=[apigateway.ThrottlingPerMethod(
        #         method=echo_method,
        #         throttle=apigateway.ThrottleSettings(
        #             rate_limit=10,
        #             burst_limit=2
        #         )
        #     )
        #     ]
        # )