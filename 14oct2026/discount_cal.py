price=int(input("enter the price:"))
discount=int(input("enter the discount:"))
discount_amount=(discount/100)*price 
print("discount amount")
print("final price:",price-discount_amount)