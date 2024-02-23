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

    if (not ('email' in user_data and 'password' in user_data and 'full_name' in user_data and 'mobile' in user_data)):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "incorrect body section",
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
            "statusCode": 400,
            "body": json.dumps({
                "message": "password format is not correct",
            }),
        }
    except boto_client.exceptions.UsernameExistsException:
        return {
            "statusCode": 409,
            "body": json.dumps({
                "message": "The client name already exists",
            }),
        }
    except ClientError as ex:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f'cognito error: {str(ex)}',
            }),
        }
    
    try:
        client = Client('client',response['UserSub'],email=user_data['email'],full_name=user_data['full_name'],mobile=user_data['mobile'])
        client.save()
    except Exception as ex:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f'pynamo error: {str(ex)}',
            }),
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": 'client succesfully signed_up',
        }),
    }
    