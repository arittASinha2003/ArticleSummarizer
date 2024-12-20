import os
import streamlit as st
from langchain_cohere.chat_models import ChatCohere
from langchain.prompts import PromptTemplate
from goose3 import Goose
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Summarization Model (Cohere)
summarization_model = ChatCohere(cohere_api_key=os.getenv("COHERE_API_KEY"), model="command-r-plus", temperature=0.5)

# Extracts useful content from a webpage using Goose
def scrape_article(url):
    g = Goose()
    article = g.extract(url=url)
    return article.cleaned_text if article else None

# Summarizes the webpage content using the model
def summarize_content(content):
    prompt_template = PromptTemplate.from_template(template="Summarize the following content:\n\n{content}\n\nSummary:")
    response = summarization_model.invoke(prompt_template.format(content=content))
    return response.content

# Answers a question based on the provided summary
def get_answer(summary, question):
    qa_prompt_template = PromptTemplate.from_template(
        template="Answer the question based on the provided summary: {summary}\n\nQuestion: {question}\n\nAnswer:"
    )
    response = summarization_model.invoke(qa_prompt_template.format(summary=summary, question=question))
    return response.content

# Streamlit Interface for Web Summarizer and Question Answering
st.title("Webpage Article Summarizer with Question Answering")
st.write("Enter a URL of a webpage to summarize its content, and ask questions based on the summary.")

# Input for URL
url_input = st.text_input("Enter the webpage URL:")

# Initialize session state to store the summary
if "summary" not in st.session_state:
    st.session_state["summary"] = ""

# Button to Summarize
if st.button("Summarize"):
    if url_input:
        with st.spinner("Extracting content..."):
            # Extract content using Goose
            raw_content = scrape_article(url_input)
        
        if raw_content:
            with st.spinner("Summarizing content..."):
                # Summarize the content
                summary = summarize_content(raw_content)
                
                # Store the summary in session state
                st.session_state["summary"] = summary
                
                # Display the summary
                # st.subheader("Summary:")
                # st.write(st.session_state["summary"])
        else:
            st.error("No content extracted from the provided URL.")
    else:
        st.warning("Please enter a valid URL.")

# Display the summary from the session state if it exists
if st.session_state["summary"]:
    st.subheader("Summary:")
    st.write(st.session_state["summary"])

    # Option to Ask a Question
    st.subheader("Ask a Question:")
    question_input = st.text_input("Enter your question:")
    
    # Button to Answer the Question
    if st.button("Get Answer"):
        if question_input:
            with st.spinner("Answering your question..."):
                # Answer the question based on the summary
                answer = get_answer(st.session_state["summary"], question_input)
                
                # Display the answer
                st.subheader("Answer:")
                st.write(answer)
        else:
            st.warning("Please enter a question to get an answer.")
