
class TheTreatShop:
    def __init__(self,biscuits,chewies,vitamins,bucket_size,is_weekend):
        self.biscuits = biscuits
        self.chewies = chewies
        self.vitamins = vitamins
        self.bucket_size = bucket_size
        self.is_weekend = is_weekend

    def calculate(self):
        print("PRICE")

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
