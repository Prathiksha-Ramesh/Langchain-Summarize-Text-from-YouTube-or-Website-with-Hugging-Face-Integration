# Langchain: Summarize Text from YouTube or Website with Hugging Face Integration

This project is a Streamlit application that integrates LangChain and Hugging Face to summarize content from YouTube videos or website URLs. The application leverages various LangChain components to load and process the content, which is then summarized using a model from Hugging Face.

## Project Structure

project-directory/ 
│ ├── app.py 
├── requirements.txt 
├── .env 
├── README.md 
├── LICENSE 
├── .gitignore 
└── Screenshot_2024-08-29_104715.png


## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/langchain-summarizer.git
cd langchain-summarizer
````

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3.Set up your Hugging Face API token in the `.env` file:

```bash
HUGGINGFACE_API_TOKEN=your_huggingface_api_token
```
Replace the placeholder with your actual Hugging Face API token.

## Running the Application

1. Ensure your `.env` file is properly configured with your Hugging Face API token.

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Open your web browser and go to `http://localhost:8501` to interact with the application.

## Example Usage
1. Enter a valid YouTube or website URL into the text input field.
2. Click the "Summarize the content from YT or website" button.
3. The application will use LangChain to load the content and Hugging Face to generate a summary of the content from the provided URL.

## Integration Details

- `LangChain Components`: Used for loading and processing text from YouTube videos or websites. LangChain's modular approach makes it easy to handle different types of content.
- `Hugging Face Integration`: The Hugging Face model is used to perform the summarization task. The model is accessed via the Hugging Face API, making it easy to experiment with different models available on the Hugging Face platform.

## Files
- `app.py`: The main Python script that handles the Streamlit interface, LangChain components, and the summarization process.
- `requirements.txt`: Lists all the Python dependencies needed to run the application.
-`.env`: Contains the Hugging Face API token. This file should not be included in version control.
- `README.md`: This file, providing an overview of the project.
- `LICENSE`: The project's license, specifying how others may use the code.
- `.gitignore`: Specifies files and directories that should be ignored by Git, such as the .env file and any other sensitive information.
- `Screenshot_2024-08-29_104715.png`: A screenshot of the interface, included for reference.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## .gitignore
The following files are ignored in the version control:

```
.env
__pycache__/
*.pyc
*.pyo
*.pyd
```

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments
Thanks to the developers of LangChain for providing powerful tools for building language model applications.
Thanks to Hugging Face for their APIs and models that make advanced NLP tasks accessible.
Screenshot

