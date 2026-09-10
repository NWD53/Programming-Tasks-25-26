"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

sent = str(input("Enter a sentence: "))
words = []
current_word = " " 
if not " " in sent:
    print("error")
def stringParser(sent):
    for char in sentence:
        if char != " ":
            current_words += char
        
        
