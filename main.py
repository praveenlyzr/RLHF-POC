from utils import magic_prompts, gpt_request, like, text_list, rag, combine_text, text_file

meta_prompt = '''You write stories for kids'''

new_prompt = magic_prompts (meta_prompt)

user_prompt = '''The crow and the sparrow became friends after being enemies for 10 years'''

result = gpt_request (system_prompt = new_prompt, user_prompt = user_prompt)

text_file (result, 'original content')

print (result)

#end of phase 1

# now lets assume user likes it....

combined_text = combine_text(meta_prompt=meta_prompt, user_prompt=user_prompt, result=result)

Like_index = like (combined_text)

# user decides to write something similar

user_prompt = '''The dragon and the sparrow became friends after being enemies for 10 years'''

test_query = f'Show me similar content like {user_prompt}'

rag_response = rag (test_query, Like_index)

print (rag_response)

prompt_with_history = f'Suggestion: {user_prompt}\nLiked History: {rag_response}'

text_file (prompt_with_history, 'new modified prompt content')

result = gpt_request (system_prompt = new_prompt, user_prompt = prompt_with_history)

print ('---FINAL SIMILAR CONTENT---')

text_file (result, 'similar content')

print (result)