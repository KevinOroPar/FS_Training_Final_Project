from models.pynamo_models import Product
from ulid import ULID
import json

def update_product(event,context):
    product_id = event['pathParameters']['product_id']
    new_data = json.loads(event['body'])
    updated = False
    

    if  ((not ('seller_id' in new_data)) or (not ('name' in new_data or 'price' in new_data or 'category' in new_data))):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "incorrect body section",
            }),
        }
    
    for product in Product.query('product', Product.SK == product_id ,Product.seller_id == new_data['seller_id']):
        if ('name' in new_data):
            product.name = new_data['name']
            product.save()
            updated = True
        if ('price' in new_data):
            product.price = new_data['price']
            product.save()
            updated = True
        if ('category' in new_data):
            product.category = new_data['category']
            product.save()
            updated = True

    if (not updated):
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "there is no product matching the entered data",
            }),
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "product succesfully updated",
        }),
    }