from models.pynamo_models import Product
import json

def get_products(event,context):
    product_list = []

    for product in Product.query('product'):        
        product_list.append({
        "id": product.SK,
        "name": product.name,
        "price": product.price,
        "category": product.category,
        "seller_id": product.seller_id
        })

    if (len(product_list) == 0):
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "there are no registered products",
            }),
        }
    
    return {
            "statusCode": 200,
            "body": json.dumps({
                "products": product_list
            }),
        }