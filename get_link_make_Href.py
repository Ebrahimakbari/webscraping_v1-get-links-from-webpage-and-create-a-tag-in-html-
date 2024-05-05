import requests
from bs4 import BeautifulSoup
import json

url = 'https://tosinso.com/courses/free-web-scraping-with-python'
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.content, 'html5lib')
script_tags = soup.find_all('script', type='application/ld+json')

# Extract contentUrl from each script tag
content_urls = []
for script_tag in script_tags:
    json_data = script_tag.string.strip()
    if json_data:
        try:
            data = json.loads(json_data)
            if '@type' in data and data['@type'] == 'VideoObject' and 'contentUrl' in data:
                content_urls.append(data['contentUrl'])
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data: {json_data}")
            print(f"Error message: {e}")

temp = '<a href="x"></a>'
with open('txt.txt', 'w') as reader:
    for url in content_urls:
        tramp = temp.replace('x', url)
        reader.write("%s\n" % (tramp))
        tramp = ''
