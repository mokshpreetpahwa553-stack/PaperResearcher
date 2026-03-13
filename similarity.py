import math
from paper import RESEARCHPAPER
#this module contains no class, it only have functions that
#use maths 

#this function computes intersection product of word frequencies

def dot_product(dict1,dict2): #intersection product of word frequencies
    freq_dict1=dict1.word_frequency()
    freq_dict2=dict2.word_frequency()
    total=0
    for word,count in freq_dict1.items():
        count2=freq_dict2.get(word,0) #if word not in dict2 then we give 0 as count
        total+=count*count2

    return total


# Treat the word counts like a vector (list of numbers).
# Magnitude = length of this vector.
# Formula: sqrt(v1^2 + v2^2 + ... + vn^2)
# We use this to remove the effect of document length
def magnitude(dict1): 

    freq_dict=dict1.word_frequency()
    total=0
    for word,count in freq_dict.items():
        total=total+pow(count,2)
    
    mag=math.sqrt(total)
    return mag

# Cosine similarity measures how similar two documents are
# by looking at the angle between their vectors.
# Result is between 0 and 1 (for word counts):
#   close to 1 -> very similar topic
#   close to 0 -> very different / unrelated
def cosine_similarity(dict1,dict2): 
    #formula: dot / (mag1 * mag2)

    dot=dot_product(dict1,dict2)
    mag1=magnitude(dict1)
    mag2=magnitude(dict2)

    if mag1==0 or mag2==0:
        return 0

    return dot/(mag1*mag2) 
