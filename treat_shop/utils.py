from treat_shop.constants import PRICES, WEEKEND_INCREASE, DISCOUNTS

def determine_price(item,item_count,bucket_size,is_weekend):
    # Get bucket item values based on bucket size
    treat_price_info = PRICES[bucket_size]
    item_price = treat_price_info[item]

    # Initiate total
    item_total = item_count * item_price

    if is_weekend == "Y":
        item_total *= (1 + WEEKEND_INCREASE)
        
    return item_total

def determine_discount_for_all(total_amount,total_treats_count,vitamins,chewies,bucket_size):
    total_amount = total_amount
    
    if (bucket_size in DISCOUNTS["total_treats"]["bucket_size"] and
            total_treats_count >= DISCOUNTS["total_treats"]["min_item_amount"]):
        total_amount *= (1 - DISCOUNTS["total_treats"]["price"])
    
    if (vitamins >= DISCOUNTS["vitamins"]["min_item_amount"] and 
            bucket_size in DISCOUNTS["vitamins"]["bucket_size"]):
        total_amount *= (1 - DISCOUNTS["vitamins"]["price"])
    
    if (chewies >= DISCOUNTS["chewies"]["min_item_amount"] and 
            bucket_size in DISCOUNTS["chewies"]["bucket_size"]):
        total_amount *= (1 - DISCOUNTS["chewies"]["price"])
    
    return total_amount