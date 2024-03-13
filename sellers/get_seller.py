from models.pynamo_models import Seller
import json

def get_seller(event,context):
    
    user_id = event['pathParameters']['user_id']
    
    try:
        seller = Seller.get('seller',user_id)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "id": seller.SK,
                "email": seller.email,
                "full_name": seller.full_name
            }),
        }
    except Exception:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "couldn't find a seller with the corresponding id",
            }),
        }