
# Article Summarizer and Question Answering Web App

This project is a web application that allows users to summarize the content of any webpage by providing its URL, and asking questions based on the summarized content and get answers.

The application is built using **Streamlit** for the web interface, **Cohere** for the natural language processing tasks (summarization and question answering), and **BeautifulSoup** for extracting the webpage content.

## Features

- **Webpage Summarization**: Enter a URL, and the app will scrape the content, summarize it using Cohere's language model, and display the summary.
- **Question Answering**: After the summary is generated, you can ask questions related to the summary, and the app will provide answers based on the summarized content.

## Requirements

To run this project locally, you need the following tools and libraries:

- **Python 3.x**
- **Cohere API Key** (Sign up for free at [cohere.com](https://cohere.com) and get your API key)
- Necessary Python libraries listed in the `requirements.txt` file.
## Libraries Used

- `streamlit`: For the web interface.
- `langchain-cohere`: For interfacing with the Cohere model.
- `cohere`: Cohere's official SDK for natural language processing.
- `requests`: For making HTTP requests to fetch webpage content.
- `beautifulsoup4`: For parsing HTML and extracting content from webpages.
- `goose3`: For extracting and parsing webpage content.
- `python-dotenv`: For managing environment variables (like the Cohere API key).

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/arittASinha2003/ArticleSummarizer.git
cd article-summarizer
```

### 2. Install Dependencies
First, ensure you have Python 3.x installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a .env file in the root of the project and add your Cohere API key:
```bash
COHERE_API_KEY=your-cohere-api-key
```
You can get your Cohere API key by signing up at [Cohere](https://dashboard.cohere.com/api-keys).

### 4. Run the Application
To start the application, run the following command:
```bash
streamlit run Article.py
```

## Acknowledgements

 - **Cohere**: For providing the natural language models used for summarization and question answering.
 - **Streamlit**: For creating an easy-to-use framework for building data applications.
 - **Goose3**: For providing a reliable tool to extract main content from webpages.
