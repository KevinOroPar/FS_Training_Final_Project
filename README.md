# Sales Platform (AWS Project) 💻

This project simulates a simple sales platform using AWS services.  It allows basic management of users, sellers, products, and purchases.

This project contains the source code and supporting files for a serverless application that you can deploy using the SAM CLI. It includes the following files and folders:

- auth — Code for the authorization Lambda functions. This code manages which users are allowed to access the endpoints based on their credentials.

- clients — Code for the client-related Lambda functions. This code handles all operations related to clients.

- models — Code representing the models for the DynamoDB database.

- products — Code for the product-related Lambda functions. This code handles all operations related to products.

- purchase — Code for the purchase-related Lambda functions. This code handles all operations related to purchases.

- sellers — Code for the seller-related Lambda functions. This code handles all operations related to sellers.

- events — Invocation events that you can use to trigger the functions.

- tests — Unit tests for the application code.

- template.yaml — A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the template.yaml file included in this project.

## Technologies Used 🔍
- **AWS Lambda** (serverless backend logic)
- **AWS API Gateway** (REST API management)
- **AWS DynamoDB** (NoSQL database for storing users, sellers, products, and purchases)
- **AWS Cognito** — User authentication and authorization.
- **AWS IAM Roles** — Secure permission management for AWS resources.

## Functionality 💡
- Users and sellers can register and manage their accounts through API endpoints.
- Products can be created, updated, listed, and deleted.
- Users can browse products and make purchases.
- All data is stored securely in DynamoDB.

## Deploy the application 🔨

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
Sales$ sam build --use-container
```

The SAM CLI installs dependencies defined in `SALES/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
Sales$ sam local start-api
Sales$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        FunctionName:
          Type: Api
          Properties:
            Path: /path
            Method: httpMethod
```