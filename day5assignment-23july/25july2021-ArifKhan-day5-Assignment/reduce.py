import functools
list= [1,2,3,4]
print(functools.reduce(lambda a, b: a+b, list))