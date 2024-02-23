from models.pynamo_models import Seller
import json

def get_seller(event,context):
    
    UserSub = event['pathParameters']['UserSub']
    for seller in Seller.query('seller',Seller.SK == UserSub):
        return {
            "statusCode": 200,
            "body": json.dumps({
                "id": seller.SK,
                "email": seller.email,
                "full_name": seller.full_name
            }),
        }
    
    return {
        "statusCode": 404,
        "body": json.dumps({
            "message": "couldn't find a seller with the corresponding UserSub",
        }),
    }