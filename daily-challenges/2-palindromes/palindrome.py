
def palindrome(word):
    return word == word[::-1]
        
with open ('words_in_english_dictionary.txt', "r") as f:
    lines = []
    for line in f:
        for word in line.split():
            if palindrome(word):
                lines.append(word)
    print (lines)

with open ("palindromes.txt", "w") as f2:
    for line in lines:
        f2.write (line + '\n')
    
    

