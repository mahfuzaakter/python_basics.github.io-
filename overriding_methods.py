class user:
    def __init__(self,user_name, total_purchase):
        self.name = user_name
        self.purchase= total_purchase

    def get_shipping_cost(self):
        if self.purchase > 1000:
           return 40
        return 60

class premiumuser(user):
    
    def get_shipping_discount(self):
        if self.purchase > 2000:
            return 100
        return 20
    def get_shipping_cost(self):  #overriding method
        # return super().get_shipping_cost()
        return 0
    

premium_user=premiumuser("mahfuza",2000)  #object create
print(premium_user.get_shipping_cost())    #object call