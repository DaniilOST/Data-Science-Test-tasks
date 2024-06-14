import math

def cosine_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        print("error.length")
        return
    
    if not any(vec1) or not any(vec2):
        print("error.null")
        return
    
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    
    norm_vec1 = math.sqrt(sum(v1 ** 2 for v1 in vec1))
    norm_vec2 = math.sqrt(sum(v2 ** 2 for v2 in vec2))
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        print("error.null")
        return
    
    cosine_similarity = dot_product / (norm_vec1 * norm_vec2)

    cosine_distance = 1 - cosine_similarity
    
    print(cosine_distance)

vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

cosine_distance(vec1, vec2)

vec1 = [0, 0, 0]
vec2 = [4, 5, 6]

cosine_distance(vec1, vec2)

vec1 = [1, 2]
vec2 = [1, 2, 3]

cosine_distance(vec1, vec2)
