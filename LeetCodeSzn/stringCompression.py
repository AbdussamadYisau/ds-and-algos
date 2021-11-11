class Solution:
    def compress(chars):
        result = ""
        # result = []
        result += chars[0]
        numberOfLetters = 1
        
        if len(chars) == 1:
            return result
        
        
        for i in range(1, len(chars)): 
            if chars[i] != chars[i-1]:
                if numberOfLetters >= 10:
                    numberOfLettersArray = str(numberOfLetters)
                    for i in numberOfLettersArray:
                        result += str(i)
                        # result.append(i)
                        
                else:
                    result += str(numberOfLetters)
                    # result.append(numberOfLetters)
                    
                result += chars[i]
                numberOfLetters = 1
            else:
                numberOfLetters += 1
        
        if numberOfLetters >= 10:
            numberOfLettersArray = str(numberOfLetters)
            for i in numberOfLettersArray:
                result += str(i)
                # result.append(i)
        else: 
            # result.append(numberOfLetters)
            result+= str(numberOfLetters)
        
        chars.append(result)
        return result

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(Solution.compress(chars))

    