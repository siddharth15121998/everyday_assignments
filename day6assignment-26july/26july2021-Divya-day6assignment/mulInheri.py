class amazon:
    def product_name(self,name):
        self.name = name
        print(self.name)
class item_num(amazon):
    def product_num(self,ordernum):
        self.ordernum = ordernum
        print(self.ordernum)
class consumer(item_num):
    def delivery(self,address,mobno):
        #self.address = address
        print(address,mobno)
objconsumer = consumer()
objconsumer.product_name("Redmi 9 pro -mobile")
objconsumer.product_num(199902)
objconsumer.delivery("xxxx",98966857)
