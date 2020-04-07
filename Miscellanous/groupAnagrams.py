from collections import defaultdict
def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
print(groupAnagrams(['lump', 'eat',  'me',  'tea', 'em', 'plum']))