text_list = []

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