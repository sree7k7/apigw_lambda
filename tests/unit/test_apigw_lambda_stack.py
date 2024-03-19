import aws_cdk as core
import aws_cdk.assertions as assertions

from apigw_lambda.apigw_lambda_stack import ApigwLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in apigw_lambda/apigw_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApigwLambdaStack(app, "apigw-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
