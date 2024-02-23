from models.pynamo_models import Purchase
import json

def get_purchases(event,context):
    purchase_list = []

    for purchase in Purchase.query('purchase'):        
        purchase_list.append({
        "id": purchase.SK,
        "client_name": purchase.client_name,
        "seller_name": purchase.seller_name,
        "product_name": purchase.product_name,
        "price": purchase.price,
        "pruchase_date": purchase.purchase_date
        })

    if (len(purchase_list) == 0):
        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "there are no registered purchases",
            }),
        }
    
    return {
            "statusCode": 200,
            "body": json.dumps({
                "purchases": purchase_list
            }),
        }