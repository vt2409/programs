# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Word Embeddings - Find similar words using Word2Vec
# Difficulty: Hard | Frequency: ⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: NATURAL LANGUAGE PROCESSING (NLP)                      ║
# ║  PURPOSE: Word embeddings using Google's pretrained Word2Vec      ║
# ║  FEATURES: Find semantically similar words, similarity scoring    ║
# ╚═══════════════════════════════════════════════════════════════╝
# Note: Requires: pip install gensim
#       First run will download ~1.5GB model (one-time)
from gensim.models import KeyedVectors

# Download Google’s pretrained Word2Vec (300-dimensions, ~1.5GB)
# Note: You only need to do this once
import gensim.downloader as api
model = api.load("word2vec-google-news-300")

similar_words = model.most_similar('apple')
for word, score in similar_words:
    print(f"{word}: {score:.4f}")