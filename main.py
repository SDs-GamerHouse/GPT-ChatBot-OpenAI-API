# Importing required libraries
import openai  
import streamlit as st
from streamlit_chat import message

# Get your own API key from the OpenAI website
from my_api_key import my_api_key

openai.api_key = my_api_key

def generate_AI_response(prompt):
    completions = openai.Completion.create(
        engine = "gpt-3.5-turbo",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    response = completions.choices[0].text
    return response

# Creating streamlit app
st.title("🤖 GPT ChatBot 🤖")

# Storing the conversation
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []

def get_prompt():
    prompt = st.text_input("You: ", "Hello, who are you?", key="input")
    return prompt

user_input = get_prompt()

if user_input:
    AI_response = generate_AI_response(prompt=user_input)
    # Storing the input and output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(AI_response)

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"])-1,-1,-1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")