# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Natural Language Processing - spaCy NER and POS tagging
# Difficulty: Hard | Frequency: ⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: NATURAL LANGUAGE PROCESSING (NLP)                      ║
# ║  PURPOSE: Advanced text analysis using spaCy library              ║
# ║  FEATURES: NER, noun phrases, POS tagging, verb extraction        ║
# ╚═══════════════════════════════════════════════════════════════╝
# Note: Requires: pip install spacy
#       Then: python -m spacy download en_core_web_sm

import spacy

nlp = spacy.load("en_core_web_sm")

text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# entitys = [entity for entity in doc.ents]
# nouns = [noun for noun in doc.noun_chunks]
# # print(nouns)
# for noun in doc.noun_chunks:
#     print(f"Noun : {noun.text} and {noun.label_}")

print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
# print(doc.ents)

# import spacy

# nlp = spacy.load("en_core_web_sm")
# tokens = nlp("dog cat banana afskfsd")

# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)
