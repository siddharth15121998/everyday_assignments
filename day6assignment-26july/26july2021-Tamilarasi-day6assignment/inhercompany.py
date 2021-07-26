class Company:
    def companyno(self,no):
        print(no)
    
class Google(Company):
    def googleproduct(self,brand,price):
        print(brand,price)


class FeedBackCustomer(Google):
    def customerFeedback(self,name,mblno,feedback):
        print(name,mblno,feedback)

obj=FeedBackCustomer()
obj.customerFeedback("tamil",9876543210,"sactified")
obj.googleproduct("Google chrome",50000)
obj.companyno(1)