import urllib.request

url1 = "http://www.baidu.com/"
f = urllib.request.urlopen(url1)
info = f.read()
#print(info.decode())
print(f.geturl())
print(f.getcode())
print(f.info())
