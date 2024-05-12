#from langchain_openai import ChatOpenAI
from langchain_community.llms import CTransformers

#llm = ChatOpenAI(api_key="")
#llama 이용
llm = CTransformers(model='llama-2-7b-chat.ggmlv3.q2_K.bin', model_type='llama')



#from langchain_core.prompts import ChatPromptTemplate
#prompt = ChatPromptTemplate.from_messages([
#    ("system", "You are a world class technical documentation writer."),
#    ("user", "{input}")
#])

#from langchain_core.output_parsers import StrOutputParser

#output_parser = StrOutputParser()

#chain = prompt | llm | output_parser

#content="LLM"



#타이틀
import streamlit as st

st.title('자료 조사 프로그램')

#텍스트 인풋
import streamlit as st

content = st.text_input("무엇이 궁금하신가요?", "")

#버튼
import streamlit as st

if st.button("검색"):
    with st.spinner('요약 중입니다...'):
        result=llm.invoke("summerize about"+content)
        st.write(result)
else:
    st.write("")