'''
Create a function, wordSplit() which takes in a spring and a set listOfWords. The function will then determine if it is possible to split the string in a way in which words can be made from the listoFWords. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
'''

def wordSplit(phrase, listOfWords, output = None):
    if output is None:
        output = []
    
    for word in listOfWords:
        if phrase.startswith(word):
            output.append(word)

            return wordSplit(phrase[len(word):], listOfWords, output)
    return output

print(wordSplit("themanran", ["the", "man", "ran"]))