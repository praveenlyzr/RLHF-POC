from utils import magic_prompts, gpt_request, like, text_list, rag, combine_text, text_file

meta_prompt = '''You Generate content'''

new_prompt = magic_prompts (meta_prompt)

user_prompt = '''The crow and the sparrow became friends after being enemies for 10 years'''

result = gpt_request (system_prompt = new_prompt, user_prompt = user_prompt)

text_file (result, 'original content')

print (result)

#end of phase 1

# now lets assume user likes it....
content = 'Shortform content (Reels, Tiktok, etc.)'

likes = '''Strong Hook: The first few seconds and lines are crucial. Get to the point quickly with an attention-grabbing statement, question, or visual.
Storytelling: Even in short videos, a simple story arc (setup, problem, resolution) can be very effective.
Clear Value Proposition: What will the viewer gain? Whether it's knowledge, humor, or inspiration, make the value clear.
Call to Action: Encourage engagement, even if it's simple ("Like for part 2," "Comment your thoughts!").
Clever Use of Captions/Overlays: Text can enhance jokes, reinforce key points, and add context.
Appropriate Use of Trending Sounds: Using a relevant trending sound can boost visibility, but only if it genuinely fits the context of your video.'''

dislikes = '''Clichéd openings: Lines like "Hey guys..." or long rambling introductions get skipped.
Too Much Text: Walls of text overwhelm viewers. Keep it concise and visually spaced if possible.
Passive Voice/Weak Language: Strong verbs and active phrasing are more engaging.
Confusing Point: If viewers don't "get it" within the short timeframe, they'll likely scroll past.
Mismatching Sound/Visuals: Jarring audio or visuals clashing with the script makes for a disjointed experience.'''

combined_text = combine_text(content=content, likes=likes, dislikes=dislikes)

Like_index = like (combined_text)

content = 'Children stories (bedtime stories, poems, etc.)'

likes = '''Repetition: Simple, repeated words, phrases, or patterns help young children learn and feel engaged.
Rhymes and Rhythm: Stories with a pleasing rhythm and rhyming structure make them memorable and fun to read aloud.
Silly Sounds and Words: Children love onomatopoeia (words that represent sounds) and made-up nonsense words that are purely for the fun of it.
Simple Dialogue: Short, easy-to-follow conversations make it easier for kids to grasp the characters and their interactions.
Humorous Situations: Age-appropriate humor that involves relatable problems, surprises, or a bit of silliness.
Relatable Characters: Children connect best with characters who experience similar emotions or challenges that they themselves can understand.
Sensory Language: Words that invoke sights, sounds, smells, touch, and taste help make the story more immersive.'''

dislikes = '''Complex Vocabulary: Overly difficult words disrupt the flow for young kids and hinder their understanding.
Long, Rambling Sentences: Keep sentences short and direct for better comprehension.
Passive Story Structure: Kids crave some form of conflict or problem-solving, even if it's a simple, everyday issue.
Abstract Concepts: Children usually do better with very concrete ideas instead of highly philosophical or abstract topics.
Morality Tales: Overly preachy or didactic stories feel less genuine and can make kids resistant.
Scary or Violent Elements: Stories that are age-inappropriate in terms of violence or extremely frightening themes can be upsetting for young children.'''

combined_text = combine_text(content=content, likes=likes, dislikes=dislikes)

Like_index = like (combined_text)

# user decides to write something similar

user_prompt = '''The dragon and the sparrow became friends after being enemies for 10 years'''

user_content = 'Children book'

test_query = f'show me the likes and dislikes that could help me with this type of content: {user_content}'

rag_response = rag (test_query, Like_index)

print (rag_response)

prompt_with_history = f'Suggestion: {user_prompt}\nLiked History: {rag_response}'

text_file (prompt_with_history, 'new modified prompt content')

result = gpt_request (system_prompt = new_prompt, user_prompt = prompt_with_history)

print ('---FINAL SIMILAR CONTENT---')

text_file (result, 'similar content')

print (result)