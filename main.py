from openai import OpenAI
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

# ChatGPT 사용법
st.write('### :orange[OpenAI API - ChatGPT 사용법]')
st.write('* MBTI 유형별 맞춤 공부법을 추천해주는 AI입니다.')

client = OpenAI(
    api_key="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"
)

question = st.text_input('본인의 MBTI를 적어주세요.', "")
gptModel = st.selectbox(
   "어떤 GPT 모델에게 답변 받고 싶은가요?",
   ("gpt-3.5-turbo", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k-0613"),
   index=None,
   placeholder="원하는 GPT 모델 선택",
) 

st.write(':violet[선택한 GPT 모델:]', gptModel)

if st.button("실행", key=1):
    with st.spinner('답변 작성중...'):
        response = client.chat.completions.create(
        model=gptModel,
        messages=[
            {"role": "system", "content": "당신은 MBTI 유형별 맞춤 공부법을 추천해주는 AI입니다. 사용자의 MBTI를 입력 받으면, 이에 맞는 맞춤 공부법을 제시해줍니다."},
            {"role": "user", "content": question}
        ]
        )
        st.write(response.choices[0].message.content)
if st.checkbox('Show Code', value=False, key='check1'):
    st.code('''
    question = st.text_input('본인의 MBTI를 적어주세요.', "")
    gptModel = st.selectbox(
        "어떤 GPT 모델에게 답변 받고 싶은가요?",
        ("gpt-3.5-turbo", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k-0613"),
        index=None,
        placeholder="원하는 GPT 모델 선택",
    )

    st.write('선택한 GPT 모델:', gptModel)

    if st.button("실행", key=1):
        with st.spinner('답변 작성중...'):
            response = client.chat.completions.create(
            model=gptModel,
            messages=[
                {"role": "system", "content": "당신은 MBTI 유형별 맞춤 공부법을 추천해주는 AI입니다. 사용자의 MBTI를 입력 받으면, 이에 맞는 맞춤 공부법을 제시해줍니다."},
                {"role": "user", "content": question}
            ]
            )
            st.write(response.choices[0].message.content)
            ''')

st.divider()

# DALL·E 3 사용법
st.write('### :blue[OpenAI API - DALL·E 3 사용법]')

imgReq = st.text_input('만들고 싶은 이미지를 설명해주세요.', "")

if st.button("실행", key=2):
    with st.spinner('답변 작성중...'):
        response = client.images.generate(
        model="dall-e-3",
        prompt=imgReq,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        image_url = response.data[0].url
        st.image(image_url, caption=imgReq, use_column_width=True)

if st.checkbox('Show Code', value=False, key='check2'):
    st.code('''
imgReq = st.text_input('만들고 싶은 이미지를 설명해주세요.', "")

if st.button("실행", key=2):
    with st.spinner('답변 작성중...'):
        response = client.images.generate(
        model="dall-e-3",
        prompt=imgReq,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        image_url = response.data[0].url
        st.image(image_url, caption=imgReq, use_column_width=True)
            ''')




