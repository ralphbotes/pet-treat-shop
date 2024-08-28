from treat_shop.constants import BUCKET_FILL
from treat_shop.utils import determine_price, determine_discount_for_all

class TheTreatShop:
    def __init__(self,biscuits,chewies,vitamins,bucket_size,is_weekend):
        self.biscuits = biscuits
        self.chewies = chewies
        self.vitamins = vitamins
        self.bucket_size = bucket_size
        self.is_weekend = is_weekend

    def calculate(self):
        total = 0.00

        # Step 1: Calculate price per treat item
        if self.biscuits > 0:
            total += determine_price("biscuits", self.biscuits, self.bucket_size,self.is_weekend)
        
        if self.chewies > 0:
            total += determine_price("chewies", self.chewies, self.bucket_size,self.is_weekend)
            
        if self.vitamins > 0:
            total += determine_price("vitamins", self.vitamins, self.bucket_size,self.is_weekend)

        # Step 2: Determine discount for all treats
        total_treats_count = self.biscuits + self.chewies + self.vitamins
        total = determine_discount_for_all(total,total_treats_count,self.vitamins,self.chewies,self.bucket_size)
        
        # Step 3: Add initial bucket fill amount
        total += BUCKET_FILL
        
        return total

def run():
    biscuits = int(input("Number of biscuits: "))
    chewies = int(input("Number of chewies: "))
    vitamins = int(input("Number of vitamins: "))
    bucket_size = input("Bucket size ('Normal'/'Large'): ")
    is_weekend = input("Is today Friday, Saturday or Sunday? ('Y'/'N'): ")

    myTreatShop = TheTreatShop(biscuits,chewies,vitamins,bucket_size,is_weekend)
    total = myTreatShop.calculate()
    formatted_total = round(total,2)
    print(formatted_total)
