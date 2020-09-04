computed_similarities = []
 

# FOR ALL WORDS IN MY vocab
for word in nlp.vocab:

    similarity = cosine_similarity(new_vector, word.vector)
    computed_similarities.append(word,similarity)

computed_similarities = sorted(computed_similarities, key=lambda item:-item[1])

# TOP 10 MOST similar words 

print([t[0]].text for t in computed_similarities[:10])

