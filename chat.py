from langchain_community.llms import Ollama
import streamlit as st
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(model = "phi3", base_url = "http://localhost:11434", verbose = True)

def sendPrompt(prompt):
    global llm
    response =llm.invoke(prompt)
    return response

st.title("Chatea con Betelgeuse")
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role" : "assistant", "content" : "Hazme una pregunta"}]
    
if prompt := st.chat_input("Tu pregunta"):
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = sendPrompt(prompt)
            print(response)
            st.write(response)
            message = {"role" : "assistant", "content" : response}
            st.session_state.messages.append(message)
