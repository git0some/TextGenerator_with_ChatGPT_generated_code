# Project Text Generator Work on project Stage 5 5 Generate random text chatgpt.py
# https://chat.openai.com/chat is your friend

import random
import nltk
from string import punctuation

def choose_most_probable_word(data_dict, head):
    possible_tails = data_dict[head]
    total_count = sum(possible_tails.values())
    probabilities = {tail: count / total_count for tail, count in possible_tails.items()}
    return max(probabilities, key=probabilities.get)

def generate_sentence(data_dict, words, sentence_length):
    first_word = random.choice(words)
    while first_word[-1] in punctuation:
        first_word = random.choice(words)
    chain = [first_word]
    for i in range(sentence_length - 1):
        head = chain[-1]
        next_word = choose_most_probable_word(data_dict, head)
        chain.append(next_word)
        if next_word[-1] in punctuation:
            break
    return " ".join(chain)

file_name = input()
f = open(file_name, "r", encoding="utf-8")
words = f.read().split()
f.close()

bigrm = list(nltk.bigrams(words))
data_dict = {}
for head, tail in bigrm:
    data_dict.setdefault(head, {})
    data_dict[head].setdefault(tail, 0)
    data_dict[head][tail] += 1


for i in range(10):
    sentence_length = 5
    sentence = generate_sentence(data_dict, words, sentence_length)
    while len(sentence.split()) < 5 or sentence[0].islower() or sentence[-1] not in punctuation:
        sentence = generate_sentence(data_dict, words, sentence_length)
    print(sentence)