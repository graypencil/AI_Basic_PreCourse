import re
import urllib.request

url = "https://bit.ly/3rxQFS4"
html = urllib.request.urlopen(url)
html_contents = str(html.read())
id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents) # 정규식 형태
print(id_results) # list의 형태

# for result in id_results:
#     print(result)