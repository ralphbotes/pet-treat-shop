PRICES = {
    "Normal": {
        "biscuits": 2.00,
        "chewies": 4.10,
        "vitamins": 2.50
    },
    "Large": {
        "biscuits": 3.75,
        "chewies": 4.50,
        "vitamins": 4.15
    }
}

BUCKET_FILL = 2.00

WEEKEND_INCREASE = 0.15

DISCOUNTS = {
    "vitamins": {
        "min_item_amount": 8,
        "bucket_size": ["Normal"],
        "price": 0.05
    },
    "chewies": {
        "min_item_amount": 10,
        "bucket_size": ["Large"],
        "price": 0.10
    },
    "total_treats": {
        "min_item_amount": 21,
        "bucket_size": ["Normal","Large"],
        "price": 0.20
    }
}