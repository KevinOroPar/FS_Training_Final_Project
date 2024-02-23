from models.pynamo_models import Product
from ulid import ULID
import json


def add_product(event,context):
    product_data = json.loads(event['body'])

    if (not ('seller_id' in product_data and 'name' in product_data and 'price' in product_data and 'category' in product_data)):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "incorrect body section",
            }),
        }
    
    product_id = str(ULID())
    try:
        product = Product('product',product_id,name=product_data['name'],price=product_data['price'],category=product_data['category'], seller_id=product_data['seller_id'])
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
            "message": "Product succesfully created",
        }),
    }