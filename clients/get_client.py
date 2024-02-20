from models.pynamo_models import Client
import json

def get_client(event,context):

    if 'UserSub' not in event['pathParameters']:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "UserSub expected in path",
            }),
        }
    
    UserSub = event['pathParameters']['UserSub']
    for client in Client.query('client',Client.SK == UserSub):
        return {
            "statusCode": 200,
            "body": json.dumps({
                "id": client.SK,
                "email": client.email,
                "full_name": client.full_name,
                "mobile": client.mobile
            }),
        }
    
    return {
        "statusCode": 404,
        "body": json.dumps({
            "message": "couldn't find a client with the correspondent UserSub",
        }),
    }