from models.pynamo_models import Seller
import json

def get_sellers(event,context):
    seller_list = []

    for seller in Seller.query('seller'):
        
        seller_list.append({
        "id": seller.SK,
        "email": seller.email,
        "full_name": seller.full_name
        })

    if (len(seller_list) == 0):
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "there are no registered sellers",
            }),
        }
    
    return {
            "statusCode": 200,
            "body": json.dumps({
                "sellers": seller_list
            }),
        }

    