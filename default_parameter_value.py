def cal_net_price(total_price, tax_price=5):    #tax price =5 eta default value
    net_prce = total_price +total_price +(tax_price/100)
    print(net_prce)

cal_net_price(100)
cal_net_price(200)
cal_net_price(300,10)#default vale re write