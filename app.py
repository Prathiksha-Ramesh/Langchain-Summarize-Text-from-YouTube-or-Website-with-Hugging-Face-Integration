import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEndpoint
import os

# Streamlit app configuration
st.set_page_config(page_title='Langchain: Summarize Text from YT or Website')
st.title('🦜 Langchain: Summarize Text from YT or Website')
st.subheader('Summarize URL')

# Hugging Face model configuration
repo_id = 'google/gemma-2-2b-it'


# Sidebar to input Hugging Face API token
with st.sidebar:
    hf_api_key = st.text_input('Huggingface API token', value="", type='password')

# Text input for the URL
generic_url = st.text_input('URL', label_visibility='collapsed')

# Prompt template for summarization
prompt_template = """
Provide the summary of the following content in 300 words:
Content: {text}"""

prompt = PromptTemplate(template=prompt_template, input_variables=['text'])

# Button to trigger the summarization process
if st.button('Summarize the content from YT or website'):
    # Validate all the inputs
    if not hf_api_key.strip() or not generic_url.strip():
        st.error('Please provide the information to get started')
    elif not validators.url(generic_url):
        st.error('Please enter a valid URL. It can be a YouTube video or a website URL.')
    else:
        try:
            with st.spinner('Waiting...'):
                # Determine the type of content based on the URL
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url], 
                        ssl_verify=False,
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
                    )

                # Load the document(s)
                documents = loader.load()

                # Initialize the LLM with the Hugging Face endpoint
                llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=150, temperature=0.7, token=hf_api_key)
                chain = load_summarize_chain(llm, chain_type="map_reduce")

                # Generate the summary using the prompt template
                summary = chain.run(input_documents=documents, prompt=prompt)

                # Display the summary
                st.subheader('Summary:')
                st.write(summary)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
