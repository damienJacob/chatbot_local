# First
import streamlit as st
from llm_local import LLM_local

with st.sidebar:
    openai_api_key = st.text_input(label="OpenAI API Key", 
                                   placeholder="Pas la peine", 
                                   key="chatbot_api_key", 
                                   type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    url = "http://localhost:1234/v1/chat/completions"
    content_type = "application/json" 
    llm = LLM_local(url, content_type)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = llm.get_response(st.session_state.messages)
    msg = response["choices"][0]["message"]
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])