arr = [("code", "100100101010100110100010"),
       ("braille", "110000111010100000010100111000111000100010"),
       ("the quick brown fox jumps over the lazy dog", 
        "011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")]

def spl(string): 
    return [string[i:i+6] for i in range(0, len(string), 6)]

d = {}
for text, code in arr:
    for c, val in zip(text, spl(code)):
        d[c] = val

mark = '000001'

def solution(s):
    string = ""
    for char in s:
        if char.isupper():
            string += mark
            char = char.lower()
        string += d[char]
    return string

for text, code in arr:
    assert solution(text) == code

