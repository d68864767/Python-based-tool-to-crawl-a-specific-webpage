```python
from bs4 import BeautifulSoup
from collections import defaultdict

class StyleAnalyzer:
    def __init__(self, styles):
        self.styles = styles
        self.style_dict = defaultdict(dict)

    def analyze_styles(self):
        for style in self.styles:
            soup = BeautifulSoup(style, 'html.parser')
            for tag in soup():
                if 'style' in tag.attrs:
                    style_properties = tag['style'].split(';')
                    for prop in style_properties:
                        if ':' in prop:
                            key, value = prop.split(':')
                            self.style_dict[tag.name.strip()][key.strip()] = value.strip()
        return self.style_dict

    def get_colors(self):
        color_dict = defaultdict(list)
        for tag, styles in self.style_dict.items():
            for style, value in styles.items():
                if 'color' in style:
                    color_dict[tag].append(value)
        return color_dict

    def get_fonts(self):
        font_dict = defaultdict(list)
        for tag, styles in self.style_dict.items():
            for style, value in styles.items():
                if 'font' in style:
                    font_dict[tag].append(value)
        return font_dict

    def get_margins_and_paddings(self):
        margin_padding_dict = defaultdict(list)
        for tag, styles in self.style_dict.items():
            for style, value in styles.items():
                if 'margin' in style or 'padding' in style:
                    margin_padding_dict[tag].append(value)
        return margin_padding_dict
```
