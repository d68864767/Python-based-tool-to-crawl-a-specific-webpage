```python
import time
from web_crawler import WebCrawler
from css_extractor import CSSEtractor
from style_analyzer import StyleAnalyzer
from documentation_generator import DocumentationGenerator
from css_file_creator import CSSFileCreator

class Optimizer:
    def __init__(self, url, openai_key):
        self.url = url
        self.openai_key = openai_key

    def optimize(self):
        start_time = time.time()

        # Step 1: Webpage Crawling
        crawler = WebCrawler(self.url)
        html_content = crawler.get_html()

        # Step 2: CSS Extraction
        extractor = CSSEtractor(html_content)
        styles = extractor.extract_styles()

        # Step 3: Style Analysis
        analyzer = StyleAnalyzer(styles)
        style_dict = analyzer.analyze_styles()

        # Step 4: Documentation Generation with GPT-4
        doc_generator = DocumentationGenerator(style_dict, self.openai_key)
        documentation_dict = doc_generator.generate_documentation()
        comment_dict = doc_generator.generate_comments()

        # Step 5: Organized CSS Reference File Creation
        file_creator = CSSFileCreator(style_dict, comment_dict)
        file_creator.create_css_file("optimized_styles.css")

        end_time = time.time()
        print(f"Optimization completed in {end_time - start_time} seconds.")

if __name__ == "__main__":
    optimizer = Optimizer("https://www.example.com", "your-openai-key")
    optimizer.optimize()
```
