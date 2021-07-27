#filter function
l1=[10,2,34,43]
l2=[10,34,2,6]
print(list(filter(lambda x:x in l1,l2)))


#lambda function
x=lambda a:a+5
print(x(5))

# #function definition
def sayHello():
     return "hello"

x=sayHello() #function calling
print(sayHello())
def sayHello(name):
    return "hello "+name
getName=input("enter name ")
print(sayHello(getName))


#function to check palindrome
def palindrome():
    str1=input("enter a string ")
    rev=str1[::-1]
    if(str1==rev):
        print("it is palindrome")
    else:
        print("not a palindrome")

palindrome()


#reduce function
import functools
li=[1,2,3,4,5]
print(functools.reduce(lambda a,b : a*b ,li))