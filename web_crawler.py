```python
import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:",errh)
            return None
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            return None
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            return None
        except requests.exceptions.RequestException as err:
            print ("Something went wrong:",err)
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.prettify()
```
