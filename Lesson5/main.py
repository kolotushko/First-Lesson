import requests
import inspect
#help(requests)
students = list()
#for method in dir(students):
    #print(method)
#print(hasaatr(students, "__iadd__"))
#print(getattr(students, "copy"))
#print(getattr(students, "append1", None))
#print(callable(requests."___title__"))
'''
r = requests.get('https://www.python.org')
print(r.status_code)
print(r.content)
'''
class CustomException(Exception):
    pass
class CustomTest:
    pass
#print(issubclass(CustomException, Exception))
#print(issubclass(CustomTest, Exception))
#print(issubclass(CustomTest, object))
#print(issubclass(Exception, object))
'''
custExc = CustomException()
cusTest = CustomTest()
print(isinstance(custExc, object))
print(isinstance(custExc, BaseException))
print(isinstance(custExc, Exception))
print(isinstance(custExc, CustomException))
print(isinstance(cusTest, CustomTest))
print(isinstance(cusTest, CustomException))
'''
'''
print(inspect.isclass(CustomException))
print(inspect.isfunction(requests.get))
print(inspect.isfunction(requests.post))
print(inspect.isfunction(requests.put))
print(inspect.ismethod(requests.patch))
print(inspect.ismodule(requests))
print(inspect.getmodule(requests))
'''


