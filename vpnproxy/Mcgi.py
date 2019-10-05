#!/data/data/com.termux/files/usr/bin/python
import sys,re
a = input()
b =re.findall('/.+H',a);b = (b[0]).split();b=b[0];

with open('index.html','r') as f:
    d = f.read()
c = str(len(d));print('''HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: '''+c+'''

'''+d)
