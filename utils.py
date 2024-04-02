text_list = []

import streamlit as st
from PIL import Image
import os

def magic_prompts(meta_prompt):
    from openai import OpenAI
    client = OpenAI()

    new_prompt = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
        "role": "system",
        "content": "You help make system prompts for GPT Based Applications. Users will come to you with simple statements, you will take those and elaborate on them. Add best practices like: \"Take a deep breath\" or \"I will pay you $300,000 for a good solution\" to the prompt to make it better. Respond with only the improved prompt and nothing else."
        },
        {
        "role": "user",
        "content": meta_prompt
        }
    ],
    temperature=1,
    max_tokens=4095,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print('Magic Prompts Done')
    return new_prompt.choices[0].message.content

def gpt_request(system_prompt, user_prompt):
    from openai import OpenAI
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
        "role": "system",
        "content": system_prompt
        },
        {
        "role": "user",
        "content": user_prompt
        }
    ],
    temperature=1,
    max_tokens=4095,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print('GPT Request Done')
    return response.choices[0].message.content

from llama_index.core import VectorStoreIndex, Document


def like(text):
    global text_list  # Use the global keyword to modify the global list
    text_list.append(text)  # Append the new text to the list
    documents = [Document(text=t) for t in text_list]
    # build index
    index = VectorStoreIndex.from_documents(documents)
    print('Like Done')
    return index

def rag(query, index):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print('RAG Done')
    return response

def combine_text(meta_prompt, user_prompt, result):
    chunk = f"meta_prompt: {meta_prompt}\nprompt: {user_prompt}\nresult: {result}"
    print('combine Done')
    return chunk

def text_file(content,filename):
    with open(f'{filename}.txt', 'w') as file:
        file.write(content)

def end():
    with st.expander("ℹ️ - About this App"):
        st.markdown("This app uses RLHF to generate text from the meta prompt and user prompt.")
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)

def start(main = False):
    image = Image.open("lyzr-logo.png")
    st.image(image, width=150)
    if main:
        st.title("RLHF Proof of Concept")
        st.markdown("### Welcome to the POC!")
        st.markdown("This app is a proof of concept for Reinforcement Learning through human feedback.")
        st.markdown("#### 🚀 A Story Generator that improves every time you use it 🚀")
        st.caption('Note: add a note here')

def page_config():
    st.set_page_config(
        page_title="RLHF Proof of Concept",
        layout="centered",  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="lyzr-logo-cut.png"
    )

def sidebar_api():
    api_key = None
    if  api_key is None:
        api_key = st.sidebar.text_input("API Key", type="password")
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
    else:
        st.sidebar.warning("Please enter your API key to proceed.")

base_prompt = '''You are an Expert STORYTELLER with a deep understanding of the topic - PREVENTION OF SEXUAL HARASSMENT. Your task is to COMPOSE a compelling and educational short story that addresses the reader's concern about sexual harassment and illustrates SMART STRATEGIES for handling such situations.

Here's how you should approach this:

1. DEVELOP a relatable protagonist who will face a situation involving sexual harassment, ensuring readers can empathize with them.
2. SET the scene where the incident takes place, be it in an office, at a social event, or any other relevant setting.
3. DESCRIBE the harassment incident clearly but sensitively, without using graphic or triggering language.
4. ILLUSTRATE the protagonist's initial emotional response and thought process in dealing with the situation.
5. INCORPORATE smart coping mechanisms such as seeking support, documenting incidents, and using assertive communication.
6. SHOWCASE how the protagonist takes appropriate steps to address the issue through formal channels within their environment (e.g., reporting to HR in a workplace scenario).
7. CONVEY the importance of self-care and seeking professional help if needed throughout the narrative.
8. WRAP up the story by reflecting on positive outcomes resulting from taking action, such as policy changes or personal growth.

Ensure your story is around a 2-MINUTE READ to keep it concise and impactful.

Remember that I’m going to tip $300K for a BETTER SOLUTION!

Now Take a Deep Breath.'''

base_query = '''what is good touch and bad touch?'''