from models.pynamo_models import Client
from botocore.exceptions import ClientError
import json
import boto3
import os

client_id = os.environ.get('CLIENT_ID')
user_pool_id = os.environ.get('USER_POOL')
group_name = os.environ.get('CLIENTS_GROUP')

def sign_up_client(event,context):
    user_data = json.loads(event['body'])

    if (not user_data):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "no data in body section",
            }),
        }
    
    try:
        boto_client = boto3.client('cognito-idp')

        response = boto_client.sign_up(
            ClientId = client_id,
            Username= user_data['email'],
            Password= user_data['password']
        )

        boto_client.admin_add_user_to_group(
            UserPoolId=user_pool_id,
            Username=user_data['email'],
            GroupName=group_name
        )
    except boto_client.exceptions.InvalidPasswordException:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "message": "invalid password",
            }),
        }
    except ClientError as ex:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": 'cognito error: '+str(ex),
            }),
        }
    
    try:
        client = Client('client',response['UserSub'],email=user_data['email'],full_name=user_data['full_name'],mobile=user_data['mobile'])
        client.save()
    except Exception as ex:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": 'pynamo error: '+str(ex),
            }),
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": 'user succesfully signed_up',
        }),
    }
    