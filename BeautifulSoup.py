import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

sum=0
url=input("Enter - ")
html=urllib.request.urlopen(url).read()
tree=ET.fromstring(html)
lst=tree.findall('comments/comment')
for item in lst:
    x=item.find('count').text
    x=int(x)
    sum=sum+x
print(sum)