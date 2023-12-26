```python
from bs4 import BeautifulSoup
import requests

class CSSEtractor:
    def __init__(self, html_content):
        self.html_content = html_content
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def extract_inline_styles(self):
        inline_styles = []
        for tag in self.soup():
            if 'style' in tag.attrs:
                inline_styles.append(tag['style'])
        return inline_styles

    def extract_linked_styles(self):
        linked_styles = []
        for link in self.soup.find_all('link', rel='stylesheet'):
            if 'href' in link.attrs:
                style_sheet_url = link['href']
                try:
                    response = requests.get(style_sheet_url)
                    response.raise_for_status()
                    linked_styles.append(response.text)
                except requests.exceptions.HTTPError as errh:
                    print ("HTTP Error:",errh)
                except requests.exceptions.ConnectionError as errc:
                    print ("Error Connecting:",errc)
                except requests.exceptions.Timeout as errt:
                    print ("Timeout Error:",errt)
                except requests.exceptions.RequestException as err:
                    print ("Something went wrong:",err)
        return linked_styles

    def extract_styles(self):
        inline_styles = self.extract_inline_styles()
        linked_styles = self.extract_linked_styles()
        return inline_styles + linked_styles
```
