from utils import magic_prompts, gpt_request, like, text_list, rag, combine_text, text_file

meta_prompt = '''You write stories for kids'''

new_prompt = magic_prompts (meta_prompt)

user_prompt = '''The crow and the sparrow became friends after being enemies for 10 years'''

result = gpt_request (system_prompt = new_prompt, user_prompt = user_prompt)

text_file (result, 'original content')

print (result)

#end of phase 1

# now lets assume user likes it....

likes = '''1. The content was simple and easy to understand.
2. The content was relatable.
3. The primary character was well developed.
4. The story was well told.
5. The story was always heart warming'''

dislikes = '''1. There were too many passive statements.
2. The story had complicated words.'''

combined_text = combine_text(user_prompt=user_prompt, likes=likes, dislikes=dislikes)

Like_index = like (combined_text)

# user decides to write something similar

user_prompt = '''The crow and the sparrow became friends after being enemies for 10 years'''

test_query = f'show me the likes and dislikes that could help me with this prompt: {user_prompt}'

rag_response = rag (test_query, Like_index)

print ("-----------------")
print ("Rag Response:")
print (rag_response)
print ("-----------------")

prompt_with_history = f'Suggestion: {user_prompt}\n Like and Dislike History of the user. (Make sure you take into account all the likes and dislikes): {rag_response}'

text_file (prompt_with_history, 'new modified prompt content')

result = gpt_request (system_prompt = new_prompt, user_prompt = prompt_with_history)

print ('---FINAL SIMILAR CONTENT---')

print (result)

text_file (result, 'similar content')

print (result)