#1
'''
import urllib.request as ur
bopener = ur.build_opener()
response = bopener.open("https://httpbin.org/get")
print(response.read())
'''
#2
'''
import requests as r
response = r.get("https://httpbin.org/get")
print(response.content)
'''
#3 Parse html site
'''
from parserhtml import ParseHTML
parser = ParseHTML("https://coinmarketcap.com/")
parser.ParseCoin("<span>", "</span>", "$")
print(parser.Result)
'''
from parserhtml import ParseHTML
parser = ParseHTML("https://bank.gov.ua/")
parser.ParseNBU("<div class='rate_kx9iSqCXBH'>", "</div>")
print(parser.Result)
