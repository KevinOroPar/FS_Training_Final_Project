from botocore.exceptions import ClientError
import json
import boto3
import os

client_id = os.environ.get('CLIENT_ID')

def log_in(event,context):
    user_data = json.loads(event['body'])

    if not ('email' in user_data and 'password' in user_data):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "incorrect body section",
            }),
        }  
    try:
        boto_client = boto3.client('cognito-idp')

        response = boto_client.initiate_auth(
            AuthFlow = 'USER_PASSWORD_AUTH',
            AuthParameters = {
                'USERNAME': user_data['email'],
                'PASSWORD': user_data['password']
            },
            ClientId = client_id
        )
    except boto_client.exceptions.NotAuthorizedException:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "message": "Incorrect username or password",
            }),
        }       
    except ClientError as ex:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f'cognito error: {str(ex)}',
            }),
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": 'logged in succesfully',
            "session_token": response['AuthenticationResult']['AccessToken'],
            "refresh_token": response['AuthenticationResult']['RefreshToken'],
            "id_token": response['AuthenticationResult']['IdToken']
        })
    }