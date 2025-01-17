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
    biscuits = -1
    chewies = -1
    vitamins = -1
    bucket_size = ""
    is_weekend = ""

    # For readability, start on a new line
    print("\n")

    while True:
        biscuits = int(input("Number of biscuits: "))
        if biscuits > 200 or biscuits < 0:
            print("Please enter a value from 0 and 200. Please try again.")
            continue
        
        chewies = int(input("Number of chewies: "))
        if chewies > 200 or chewies < 0:
            print("Please enter a value from 0 and 200. Please try again.")
            continue
        
        vitamins = int(input("Number of vitamins: "))
        if vitamins > 200 or vitamins < 0:
            print("Please enter a value from 0 and 200. Please try again.")
            continue

        bucket_size = input("Bucket size ('Normal'/'Large'): ").capitalize()
        if not bucket_size in ["Normal","Large"]:
            print("Only 'Normal' or 'Large' is allowed. Please try again.")
            continue

        is_weekend = input("Is today Friday, Saturday or Sunday? ('Y'/'N'): ").capitalize()
        if not is_weekend in ["Y","N"]:
            print("Only 'Y' or 'N' is allowed. Please try again.")
            continue

        # All passed
        break

    myTreatShop = TheTreatShop(biscuits,chewies,vitamins,bucket_size,is_weekend)
    total = myTreatShop.calculate()
    formatted_total = round(total,2)
    print(formatted_total)
