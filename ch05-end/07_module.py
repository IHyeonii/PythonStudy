import urllib
import urllib.request

target = urllib.request.urlopen('https://www.google.com')
result = target.read()

print(result)