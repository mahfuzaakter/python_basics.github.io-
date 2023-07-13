item_price =[10,20,30,40,50]
total_budget=500
total_count =0
#490 470 440 400 350
for current_item_price in item_price:
    total_budget -= current_item_price
    if total_budget<0:
        break
    total_count += 1
print(total_count)    