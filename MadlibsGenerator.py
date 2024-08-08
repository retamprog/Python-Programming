# project 3-Madlibs Generator
#
# A Mad Libs generator is an interactive game or tool that
# allows users to create silly and humorous stories
# by filling in blanks with different parts of speech, such as nouns, verbs, adjectives, and adverbs.
# The basic premise is:
# 1) A short story or passage is provided with certain words missing, represented by blanks or word types.
# 2) The user is prompted to supply words to fill in the blanks, without knowing the full context of the story.
# 3) Once all the blanks are filled, the story is revealed with the user's words inserted,
# often resulting in a nonsensical or absurd narrative.
# The name "Mad Libs" comes from the original book series of the same name,
# created by Leonard Stern and Roger Price in the 1950s.
# However, the concept has since been adapted into various digital formats,
# including websites, mobile apps, and even voice assistants.
with open('Madlibs/story.txt', 'r') as f:
    story = f.read()

words = set()
start_index = -1
for idx, char in enumerate(story):
    if char == '{':
        start_index = idx
    if char == '}':
        words.add(story[start_index:idx + 1])
        start_index = -1

# now we take input from the user for each of those words and store it in a dictionary and replace them in the story.
answers = {}
for word in words:
    answer = input(f'Enter a word for the following {word}: ')
    answers[word] = answer

# print(answers)
for word in words:
    story = story.replace(word, answers[word])

print(story)
