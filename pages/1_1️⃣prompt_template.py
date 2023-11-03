import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate

from langchain.prompts import(
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# API KEY 등록
os.environ["OPENAI_API_KEY"] = "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"

# Prompt Template 사용법
st.write('### :green[GPT-3 Prompt Template]')
'* :blue[PromptTemplate 예제]'
st.caption('Prompt Template: 매개변수 삽입 가능한 문자열로 변환')
davinch3 = OpenAI(
    model_name = "text-davinci-003",
    max_tokens = 1000    
)
mbti = st.text_input('본인의 MBTI 입력', "")
# #프롬프트 템플릿을 통한 매개변수 삽입 가능한 문자열로 변환
str_prompt = PromptTemplate.from_template("{mbti}의 장점 알려줘")

# #매개변수 삽입한 결과를 str_prompt_value에 할당
str_prompt_value = str_prompt.format_prompt(mbti=mbti)
if st.button("실행", key='pt'):
    with st.spinner('답변 작성중...'):
        st.write('질문 :', str_prompt_value.to_string())
        st.write(davinch3.predict(str_prompt_value.to_string()))

if st.checkbox('Show Code', value=False, key='check1'):
    st.code('''
    from langchain.prompts import PromptTemplate, ChatPromptTemplate
            
    davinch3 = OpenAI(
        model_name = "text-davinci-003",
        max_tokens = 1000    
    )
    mbti = st.text_input('본인의 MBTI 입력', "")
    # #프롬프트 템플릿을 통한 매개변수 삽입 가능한 문자열로 변환
    str_prompt = PromptTemplate.from_template("{mbti}의 장점 알려줘")

    # #매개변수 삽입한 결과를 str_prompt_value에 할당
    str_prompt_value = str_prompt.format_prompt(mbti=mbti)
    if st.button("실행", key='pt'):
        with st.spinner('답변 작성중...'):
            st.write('질문 :', str_prompt_value.to_string())
            st.write(davinch3.predict(str_prompt_value.to_string()))
            ''')
    
'* :blue[PromptTemplate 활용]'

template = """
당신은 요리사입니다. 냉장고에 있는 재료로 만들수 있는 요리를 추천해주고,
그 요리의 레시피를 따라하기 쉽게 알려주세요.

<재료>
{ingredients}
"""
ingredients = st.text_input('냉장고에 있는 재료 입력', "")

prompt_template = PromptTemplate(
    input_variables=['ingredients'],
    template=template
)
if st.button("실행", key='temp'):
    with st.spinner('레시피 작성중...'):
        question = prompt_template.format(ingredients = ingredients)
        st.write(davinch3(question))


if st.checkbox('Show Code', value=False, key='check2'):
    st.code('''
from langchain.prompts import PromptTemplate, ChatPromptTemplate
            
    template = """
당신은 요리사입니다. 냉장고에 있는 재료로 만들수 있는 요리를 추천해주고,
그 요리의 레시피를 따라하기 쉽게 알려주세요.

<재료>
{ingredients}
"""
ingredients = st.text_input('냉장고에 있는 재료 입력', "")

prompt_template = PromptTemplate(
    input_variables=['ingredients'],
    template=template
)
if st.button("실행", key='temp'):
    with st.spinner('레시피 작성중...'):
        question = prompt_template.format(ingredients = ingredients)
        st.write(davinch3(question))
            ''')

st.divider()

st.write('### :green[ChatGPT Prompt Template]')
'* :blue[ChatGPT로 Prompt Template 활용]'

chatgpt = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

chat_ingredients = st.text_input('ChatGPT에게 냉장고에 있는 재료 입력', "")

# ChatGPT에게 역할 부여
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 사용자가 입력할 매개변수 template 선언
human_message_prompt = HumanMessagePromptTemplate.from_template(chat_ingredients)

# ChatPromptTemplate에 system message와 human message 삽입
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

if st.button("실행", key='chat_temp'):
    with st.spinner('레시피 작성중...'):
        answer = chatgpt(chat_prompt.format_prompt(ingredients=chat_ingredients).to_messages())
        st.write(answer.content)

if st.checkbox('Show Code', value=False, key='check3'):
    st.code('''
from langchain.prompts import(
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
chatgpt = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

chat_ingredients = st.text_input('ChatGPT에게 냉장고에 있는 재료 입력', "")

# ChatGPT에게 역할 부여
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 사용자가 입력할 매개변수 template 선언
human_message_prompt = HumanMessagePromptTemplate.from_template(chat_ingredients)

# ChatPromptTemplate에 system message와 human message 삽입
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

if st.button("실행", key='chat_temp'):
    with st.spinner('레시피 작성중...'):
        answer = chatgpt(chat_prompt.format_prompt(ingredients=chat_ingredients).to_messages())
        st.write(answer.content)
            ''')