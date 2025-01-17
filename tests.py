"""
6 -
# Palindrome check
def is_palindrome(s: str) -> bool:
    s_alnum = "".join(str(char for char in s if char.isalnum()))
    s_alnum_reverse = s[::-1]
    if s_alnum == s_alnum_reverse:
        return True
    else:
        return False
"""
"""
# Find Missing Number in a List:

numbers = [1, 3, 2, 5]

def missin_number(numbers: list[int]) -> int:
    numbers.sort()
    for i in range(len(numbers)):
        if numbers[i] != i+1:
            return i+1
    return -1
print(missin_number(numbers))

"""

"""
8. Count Unique Characters:

def uniques_chars(palabra: str) -> dict:
    count = {} ## {"char": int}
    for char in palabra:
        if char in list(count.keys()):
            count[char] = count[char] + 1
        else:
            count[char] = 1
    return 
"""


"""
# 9. Anagrams Check:

def anagram_check(s1: str, s2: str) -> bool:
    unique1 = []
    unique2 = []

    for char1 in s1:
        if not char1 in unique1:
            unique1.append(char1)

    for char2 in s2:
        if not char2 in unique2:
            unique2.append(char2)

    if len(unique1) != len(unique2):
        return False

    for char in unique1:
        if not char in unique2:
            return False
        return True
"""

"""
# 10 Validate Parentheses

def validate_Partentheses(strings: str) -> bool:

    hash = {"(" : ")", "{":"}", "[":"]"}
    hash_invertido = {")": "(", "}":"{", "]":"["}
    reten = []
    for char in strings:
        if char in list(hash.keys()):
            reten.append(char)
        elif char in list(hash_invertido.keys()) and reten[-1] == hash_invertido.get(char):
            reten.pop()
        
    if len(reten) == 0:
        return True
    else:
        return False
    
strings = "([)"

print(validate_Partentheses(strings))
"""

# Diccionario de ejemplo
mi_diccionario = {'a': 3, 'b': 1, 'c': 2}

# Ordenar por valores en orden ascendente
diccionario_ordenado = dict(sorted(mi_diccionario.items(), key=lambda item: item[1]))
print(diccionario_ordenado)  # Salida: {'b': 1, 'c': 2, 'a': 3}