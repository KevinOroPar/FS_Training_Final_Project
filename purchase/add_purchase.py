from models.pynamo_models import Purchase
from ulid import ULID
import json


def add_purchase(event,context):
    purchase_data = json.loads(event['body'])

    if (not ('client_name' in purchase_data and 'seller_name' in purchase_data and 'product_name' in purchase_data and 'price' in purchase_data and 'purchase_date' in purchase_data)):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "incorrect body section",
            }),
        }
    
    purchase_id = str(ULID())
    try:
        product = Purchase('purchase',purchase_id,client_name=purchase_data['client_name'],seller_name=purchase_data['seller_name'],product_name=purchase_data['product_name'],price=purchase_data['price'],purchase_date=purchase_data['purchase_date'])
        product.save()
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
            "message": "Purchase succesfully created",
        }),
    }