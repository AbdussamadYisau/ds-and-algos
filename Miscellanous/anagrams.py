# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

def anagram(s1, s2):
	# Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

    #Return boolean if the two strings are anagrams
    else:
       return sorted(s1) == sorted(s2)

print(anagram("dog", "god")) #True

print(anagram("do", "dog")) # False

print(anagram("aa", "aaa")) # False, edge case  
