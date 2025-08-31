
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("Language Translator using Mistral AI")

text = st.text_area("Enter Text to Translate:", "")
languages = [
    "French", "Spanish", "German", "Chinese", "Japanese", "Hindi", "Arabic", 
    "Russian", "Portuguese", "Italian", "Korean", "Turkish", "Dutch", "Greek",
    "Swedish", "Polish", "Thai", "Indonesian", "Czech", "Hebrew", "Danish",
]

language = st.selectbox(
    "Select the language you want to translate into:", 
    languages
)


if st.button("Translate"):
    with st.spinner("Translating..."):
        system_message = (
            "You are a language translator. "
            "Translate the text given by user into the language given by the user specified after the text"
        )
        prompt = ChatPromptTemplate.from_messages(
            [("system", system_message),
             ("user", "Text:{text} \n Language:{language}")]
        )
        model = init_chat_model("mistral-large-latest", model_provider="mistralai")
        llm_chain = prompt | model | StrOutputParser()
        result = llm_chain.invoke({"text": text, "language": language})
        st.markdown("### Translated Text:")
        st.success(result)
