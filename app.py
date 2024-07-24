from dotenv import load_dotenv
load_dotenv()
import streamlit as st

import os

import google.generativeai as genai

print(os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to load Gemini pro model and get response 


model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[
    {
        'role': 'user',
        'parts': ['You are a helpful assistant.']
    },
])


def get_response(question):
    print("Reached")
    response=chat.send_message(question,stream=True)
    print(response)
    return response


st.set_page_config(page_title="Q&A Demo",page_icon="🤖")

st.header("Gemini Pro Chatbot LLM Application ")



#initialize session state for chat history if does't exist


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input=st.text_input("Input :",key="input")
submit=st.button("Ask the qeustion ")



if submit and input:
    response=get_response(input)
    ## add the chat history to session state
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is :"  )

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini Pro BOT",chunk.text))
    


st.subheader("The Chat History is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")
 



