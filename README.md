# CSS Style Extractor and Documenter

This project is a Python-based tool that crawls a specific webpage, extracts its prominent CSS styles, and then summarizes and documents these styles using OpenAI's GPT-4. The tool analyzes elements like colors, fonts, and other CSS properties, and generates a well-organized and commented CSS reference file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The project requires Python 3.6+ and the following Python libraries installed:

- BeautifulSoup
- Requests
- Selenium
- OpenAI
- Flask
- Pytest
- Numpy
- Gunicorn

You can install these dependencies using the requirements.txt file as follows:

```
pip install -r requirements.txt
```

### Project Structure

The project has the following file structure:

- `app.py`: The main Flask application file that integrates all other modules.
- `web_crawler.py`: Contains the `WebCrawler` class for fetching HTML content from a given URL.
- `css_extractor.py`: Contains the `CSSExtractor` class for parsing HTML content and extracting CSS rules.
- `style_analyzer.py`: Contains the `StyleAnalyzer` class for analyzing the extracted CSS rules and identifying key style attributes.
- `documentation_generator.py`: Contains the `DocumentationGenerator` class for generating natural language documentation for each extracted style using OpenAI's GPT-4.
- `css_file_creator.py`: Contains the `CSSFileCreator` class for creating a CSS file containing all extracted styles, organized by UI components.
- `test.py`: Contains test cases for the tool.
- `optimizer.py`: Contains code for optimizing the tool's performance.
- `deploy.py`: Contains code for preparing the tool for deployment.
- `README.md`: This file, containing information about the project and instructions for setting it up.

### Running the Application

To run the application, execute the following command in the project's root directory:

```
python app.py
```

This will start a Flask server on your local machine. You can interact with the application by sending a POST request to the `/extract_css` endpoint with a JSON body containing the `url` key and the webpage URL as the value.

## Testing

To run the tests, execute the following command in the project's root directory:

```
pytest test.py
```

## Deployment

The application can be deployed using Gunicorn. More details can be found in the `deploy.py` file.

## Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/)
- [Selenium](https://www.selenium.dev/)
- [OpenAI](https://www.openai.com/)
- [Pytest](https://docs.pytest.org/)
- [Numpy](https://numpy.org/)
- [Gunicorn](https://gunicorn.org/)

## Authors

- Your Name

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
