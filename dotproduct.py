# Calcuates the dot product

def dotProduct(vector1, vector2):
    if(len(vector1) != len(vector2)):
        exit("Error: Lengths do not match!")
        return
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

v1 = [1, 2, 3]
v2 = [4, 2, 5,3]

print(dotProduct(v1, v2))