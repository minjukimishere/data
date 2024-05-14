#from dotenv import load_dotenv
#load_dotenv()

import streamlit as st
import tempfile
import os
    

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# import question
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI

#챗봇
from langchain.chains import RetrievalQA

#제목
st.title("ChatPDF")
st.write("---")

import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

#Split
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=300,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

texts= text_splitter.split_documents(pages)

#Embedding DB에 저장할 수 있는 형태로 변환
from langchain_openai import OpenAIEmbeddings
embeddings_model = OpenAIEmbeddings(api_key="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")


#Question
st.header("PDF에게 질문해보세요")
question=st.text_input("질문을 입력하세요")

if st.button('질문하기'):
    llm = ChatOpenAI(api_key="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", temperature=0) #무작위성
    qa_chain=RetrievalQA.from_chain_type(llm,retriever=db.as_retriever())
    result=qa_chain.invoke({"query":question})
    st.write(result)


