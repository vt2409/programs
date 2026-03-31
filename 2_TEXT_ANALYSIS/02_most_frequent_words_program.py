# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: TEXT ANALYSIS & WORD PROCESSING                        ║
# ║  PURPOSE: Extract and rank most frequent words from reviews       ║
# ║  FEATURES: Punctuation removal, stop word filtering, frequency    ║
# ╚═══════════════════════════════════════════════════════════════╝

reviews = [
    "The food is great The service is amazing.",
    "great food but the service could be bette",
    "Amazing place with great food and friendly staff"
]
k = 3
ignore_punctation = ["is", "the", "a", "an", "and", "to", "in", "on", "at", "of", "for", "with", "as", "this", "that"]
import re
review_list = []
#Remove the puntation and extract the preety sting only.
for sentence in reviews:
    substring = re.sub(r"[^\w\s]",'',sentence)
    for word in substring.split(" "):
        if not word.lower() in ignore_punctation:
            review_list.append(word.lower()) 

word_freq = {}

for word in review_list:
    word_freq[word] = word_freq.get(word,0) +1

#sort the dict based on value with reverse order
sorted_dict = sorted(word_freq.items(),key=lambda x: (-x[1],x[0]))
result = dict(sorted_dict[:3])
print(result)





#convert paragraph into sentences and filter the punctation



