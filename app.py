```python
from flask import Flask, request, jsonify
from web_crawler import WebCrawler
from css_extractor import CSSExtractor
from style_analyzer import StyleAnalyzer
from documentation_generator import DocumentationGenerator
from css_file_creator import CSSFileCreator

app = Flask(__name__)

@app.route('/extract_css', methods=['POST'])
def extract_css():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        # Step 1: Webpage Crawling
        crawler = WebCrawler(url)
        html_content = crawler.get_html()

        # Step 2: CSS Extraction
        extractor = CSSExtractor(html_content)
        css_rules = extractor.get_css_rules()

        # Step 3: Style Analysis
        analyzer = StyleAnalyzer(css_rules)
        style_attributes = analyzer.get_style_attributes()

        # Step 4: Documentation Generation with GPT-4
        doc_generator = DocumentationGenerator(style_attributes)
        documentation = doc_generator.generate_documentation()

        # Step 5: Organized CSS Reference File Creation
        file_creator = CSSFileCreator(style_attributes)
        css_file = file_creator.create_css_file()

        return jsonify({
            'documentation': documentation,
            'css_file': css_file
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
