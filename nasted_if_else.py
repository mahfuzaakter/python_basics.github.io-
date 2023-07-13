user_area ='gazipur'
total_purchase_price = 1000

if user_area in ["gazipur","kapasia","sreepur"]:
    if total_purchase_price >=600:
        print("shipping free")
    elif total_purchase_price>=300 and total_purchase_price<600:
        print(" shipping price 80")    

elif user_area in ["konabari","tongi"]:
    if total_purchase_price>= 800:
        print("shipping free")
    elif total_purchase_price>=300 and total_purchase_price<800:
        print("shipping cost 100")     


else:
    print("current shipping")    