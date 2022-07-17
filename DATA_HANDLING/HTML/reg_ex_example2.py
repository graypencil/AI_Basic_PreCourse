import re
import urllib.request

url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("UTF8"))

url_list = re.findall(r"(http)(.+)(zip)", html_contents)

for url in url_list:
    print("".join(url))