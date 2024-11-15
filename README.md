# Oxido Article Processor
A simple Python application that connects to the OpenAI API, reads a text file containing an article, processes it according to specified guidelines, and generates HTML files for preview.

<h3>This application performs the following tasks:</h3>

- Connects to the OpenAI API to leverage AI capabilities.
- Downloads a text file containing an article from a specified URL.
- Reads the article content from the downloaded file.
- Sends the article to OpenAI with specific prompts for processing.
- Receives processed HTML content that adheres to the following guidelines:
- Uses appropriate HTML tags for content structuring.
- Identifies where images should be inserted using ```<img src="image_placeholder.jpg" alt="...">```.
- Includes alt attributes in ```<img>``` tags with prompts for image generation.
- Places captions under images using appropriate HTML tags.
- Saves the processed content into artykul.html.
- Generates an HTML template szablon.html with an empty ```<body>``` ready for content insertion.
- Creates a full preview podglad.html by inserting the processed content into the template.
---
<h3>Features:</h3>

- Interaction with the OpenAI API using the latest methods.
- Robust error handling with informative messages.
- Organized project structure for maintainability.
- Unit tests for critical functions.
---
<h3>Requirements:</h3>

- Python 3.7 or higher
- An OpenAI API key
---
<h3>Installation:</h3>

```
git clone https://github.com/your_username/project_name.git
```

```
cd project_name
```

```
python -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

<b>Setup</b>
Create a ```.env``` file
```
touch .env
```
Add OpenAI API key to the .env file
```OPENAI_API_KEY=your_openai_api_key_here```
---
<h3>Testing:</h3>
python -m unittest discover tests