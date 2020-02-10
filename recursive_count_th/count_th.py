'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: # If the word is under 2 characters it can't contain th
        return 0 
    elif word[:2] == "th": # Checking a slice of the first two characters
        return 1 + count_th(word[2:]) # Move ahead two characters since the first two are th
    else: 
        return count_th(word[1:]) #M Move ahead one character and try again
    pass
