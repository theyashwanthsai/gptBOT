import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import openai 

st.set_page_config(page_title="gptBOT")

with st.sidebar:
    st.title('gptBOT')
    st.markdown('''
    ## About
    Chatbot built using HugCHat API:
    - [Streamlit](https://streamlit.io/)
    - [OpenAI API]()
   
    
    💡 Note: API key is required!
    ''')
    
    openai.api_key = st.text_input("Your API key here")
    add_vertical_space(5)
    st.write('Made by Sai Yashwanth. Follow me [Twitter](https://twitter.com/yashwanthsai29) and [Github](https://github.com/theyashwanthsai)')


def generate_api_response(prompt):
        completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
        message = completions.choices[0].text
        return message 
    
   




if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi, How may I help you?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']


input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()


def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

with input_container:
    user_input = get_text()

def generate_response(prompt):
    if openai.api_key:
        output = generate_api_response(prompt)
        return output
    else:
        output = "Provide the key please"
        return output

with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))