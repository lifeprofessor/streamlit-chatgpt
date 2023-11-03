import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# from dotenv import load_dotenv
# load_dotenv()

# GPT-3 사용법
st.write('### :orange[GPT-3]')

davinch3 = OpenAI(model_name="text-davinci-003")
question = st.text_input('GPT-3에게 질문할 내용 입력', "")

if st.button("실행"):
    with st.spinner('답변 작성중...'):
        answer = davinch3.predict(question)
        st.write(answer)

if st.checkbox('Show Code', value=False, key='check1'):
    st.code('''        
    from langchain.llms import OpenAI
            
    davinch3 = OpenAI(model="text-davinci-003")
    question = st.text_input('GPT-3에게 질문할 내용 입력', "")

    if st.button("실행", key=gpt3):
        with st.spinner('답변 작성중...'):
            answer = davinch3.predict(question)
            st.write(answer)
            ''')

st.divider()

st.write('### :orange[ChatGPT]')
'* :blue[매개변수 조절]'
st.caption('temperature: 0~2 사이의 값으로 값이 작을수록 답변이 동일하고 커질수록 다양한 답변해준다.')

temperature = st.slider('temperature', 0.0, 2.0, 1.0)
chatgpt_question = st.text_input('ChatGPT에게 질문할 내용 입력', "")
chatgpt_answer = " "
if st.button("실행", key=1):
    with st.spinner('답변 작성중...'):
        chatgpt = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature)
        chatgpt_answer = chatgpt.predict(chatgpt_question)
        st.write(chatgpt_answer)

if st.checkbox('Show Code', value=False, key='check2'):
    st.code('''
    from langchain.chat_models import ChatOpenAI
            
    temperature = st.slider('temperature', 0.0, 2.0, 1.0)
    chatgpt_question = st.text_input('ChatGPT에게 질문할 내용 입력', "")
    chatgpt_answer = " "
    if st.button("실행", key=1):
        with st.spinner('답변 작성중...'):
            chatgpt = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature)
            chatgpt_answer = chatgpt.predict(chatgpt_question)
            st.write(chatgpt_answer)
            ''')

st.write('')
'* :blue[답변을 타이핑하듯이 나오도록 작성]'
st.caption('streaming: 실시간으로 답변을 타이핑하듯이 제공한다.')

chatgpt_stream = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)
chatgpt_stream_question = st.text_input('ChatGPT에게 실시간 질문할 내용 입력', "")
chatgpt_stream_answer = " "
if st.button("실행", key=2):
    with st.spinner('답변 작성중...'):
        chatgpt_stream_answer = chatgpt_stream.predict(chatgpt_stream_question)
        st.write(chatgpt_stream_answer)

if st.checkbox('Show Code', value=False, key='check3'):
    st.code('''
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
            
    chatgpt_stream = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)
    chatgpt_stream_question = st.text_input('ChatGPT에게 실시간 질문할 내용 입력', "")
    chatgpt_stream_answer = " "
    if st.button("실행", key=2):
        with st.spinner('답변 작성중...'):
            chatgpt_stream_answer = chatgpt_stream.predict(chatgpt_stream_question)
            st.write(chatgpt_stream_answer)
            ''')


# # chatGPT 역할 부여
'* :blue[ChatGPT에게 역할 부여]'
st.caption('messages: system에게 역할부여, human의 질문, AI의 답변')

chatgpt_role = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)
chatgpt_role_question = st.text_input('MBTI 유형별 맞춤 공부법 추천 AI에게 질문할 내용 입력', "")
chatgpt_stream_answer = " "
if st.button("실행", key=3):
    with st.spinner('답변 작성중...'):
        messages = [
            SystemMessage(
                content="당신은 MBTI 유형별 맞춤 공부법을 추천해주는 AI입니다. 사용자의 MBTI를 입력 받으면, 이에 맞는 맞춤 공부법을 제시해줍니다."
            ),
            HumanMessage(
                content=chatgpt_role_question
            ),    
        ]
        chatgpt_role_answer = chatgpt_role(messages)
        st.write(chatgpt_role_answer.content)

if st.checkbox('Show Code', value=False, key='check4'):
    st.code('''
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import AIMessage, HumanMessage, SystemMessage
            
chatgpt_role = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)
chatgpt_role_question = st.text_input('MBTI 유형별 맞춤 공부법 추천 AI에게 질문할 내용 입력', "")
chatgpt_stream_answer = " "
if st.button("실행", key=3):
    with st.spinner('답변 작성중...'):
        messages = [
            SystemMessage(
                content="당신은 MBTI 유형별 맞춤 공부법을 추천해주는 AI입니다. 사용자의 MBTI를 입력 받으면, 이에 맞는 맞춤 공부법을 제시해줍니다."
            ),
            HumanMessage(
                content=chatgpt_role_question
            ),    
        ]
        chatgpt_role_answer = chatgpt_role(messages)
        st.write(chatgpt_role_answer.content)
    '''
    )
