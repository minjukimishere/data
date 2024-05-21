README.md
자료 조사 프로그램
이 프로젝트는 사용자가 입력한 주제에 대해 OpenAI의 GPT-4 모델을 사용하여 자료를 조사하고 요약해주는 Streamlit 애플리케이션입니다.

주요 기능
사용자 입력을 받아 자료 조사를 수행
OpenAI의 GPT-4 모델을 사용하여 자료를 요약
결과를 화면에 출력
설치 방법
1. 필수 패키지 설치
이 프로젝트는 Python 3.8 이상이 필요합니다. 필요한 패키지는 requirements.txt 파일을 통해 설치할 수 있습니다.

bash
코드 복사
pip install -r requirements.txt
2. .env 파일 설정
.env 파일을 프로젝트 루트 디렉토리에 생성하고, OpenAI API 키를 설정합니다.

makefile
코드 복사
OPEN_API_KEY=your_openai_api_key
실행 방법
bash
코드 복사
streamlit run app.py
코드 설명
환경 변수 로드
python
코드 복사
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv('OPEN_API_KEY')
.env 파일에서 OpenAI API 키를 로드합니다.

GPT-4 모델 설정
python
코드 복사
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key=api_key)
GPT-4 모델을 사용하기 위해 ChatOpenAI 라이브러리를 설정합니다.

프롬프트 템플릿 설정
python
코드 복사
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])
모델이 사용할 프롬프트 템플릿을 설정합니다.

출력 파서 설정
python
코드 복사
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
모델 출력을 문자열로 파싱하기 위한 파서를 설정합니다.

체인 구성
python
코드 복사
chain = prompt | llm | output_parser
프롬프트 템플릿, GPT-4 모델, 출력 파서를 체인으로 연결합니다.

Streamlit UI 설정
python
코드 복사
import streamlit as st

st.title('자료 조사 프로그램')
content = st.text_input("무엇이 궁금하신가요?", "")

if st.button("검색"):
    with st.spinner('요약 중입니다...'):
        result = chain.invoke({"input": content + "에 대한 자료조사 결과를 500자 이상의 한글로 요약해줘"})
        st.write(result)
else:
    st.write("")
Streamlit을 사용하여 사용자 인터페이스를 설정합니다.

사용 방법
텍스트 입력 필드에 조사할 내용을 입력합니다.
"검색" 버튼을 클릭합니다.
GPT-4 모델이 입력한 내용을 기반으로 자료를 조사하고 요약합니다.
요약 결과가 화면에 표시됩니다.
라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.

기여
기여를 환영합니다! 버그 보고, 기능 제안 또는 PR을 통해 기여할 수 있습니다.

이 프로젝트에 대한 자세한 내용은 프로젝트 저장소를 참조하세요.