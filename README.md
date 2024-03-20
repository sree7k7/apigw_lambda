
# Welcome to your CDK Python project!

## Get method

Lambda function for get method. The code is uploaded to lambda, and the result will appear. The code will be automatically uploaded to Lambda by the CDK.

## Post methohd.
You have to pass the value of the body to the lambda function, such as: key=value or {"key": "value"} pair

## apigw with keys

- create apigw.
- add get, post methods.
- create usage plan.
- create api keys.
- Associate usage plan to api_keys: Add usage plan.
- In usage plan check associated api_keys.
