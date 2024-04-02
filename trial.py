import streamlit as st
import os
from utils import magic_prompts, gpt_request, like, text_list, rag, combine_text, text_file, end, start, sidebar_api, page_config, base_prompt, base_query

page_config()
sidebar_api()

if 'prompt' not in st.session_state:
    st.session_state['prompt'] = base_prompt

if 'query' not in st.session_state:
    st.session_state['query'] = base_query

st.sidebar.header('Navigation')

current_page = st.sidebar.radio(
    "Use a meta prompt and then proceed to the query",
    ["Introduction", "Base Prompt", "Story Teller"],
    key='current_page' 
)

if current_page == 'Introduction':
    start(True)

if current_page == 'Base Prompt':
    start(False)
    st.session_state['prompt'] = st.text_area(
        "Edit the instruction as needed:", 
        value=st.session_state['prompt']
    )

if current_page == 'Story Teller':
    start(False)
    st.session_state['query'] = st.text_area(
        "Enter your question here:", 
        value=st.session_state['query']
    )
    response = None
    st.session_state['first_time'] = True
    if st.button('Submit'):
        if st.session_state['first_time'] == False:
            user_prompt = st.session_state['prompt']
            test_query = f'Show me similar content like {user_prompt}'
            rag_response = rag (test_query, st.session_state['like_index'])
            prompt_with_history = f'Suggestion: {user_prompt}\nLiked History: {rag_response}'
            response = gpt_request(st.session_state['prompt'], prompt_with_history)
        if st.session_state['first_time'] == True:
            response = gpt_request(st.session_state['prompt'], st.session_state['query'])
        st.text_area("Here is the story teller's response: ", value=response)
    if response:
        if st.button('Like'):
            st.session_state['first_time'] = False
            combined_text = combine_text(meta_prompt=st.session_state['prompt'], user_prompt=st.session_state['query'], result=response)
            Like_index = like(response)
            st.session_state['like_index'] = Like_index


end()