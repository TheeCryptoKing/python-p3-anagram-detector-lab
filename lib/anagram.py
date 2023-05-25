# your code goes here!

class Anagram:
    def __init__(self, word="word"):
        self.word = word
    
    def match(self, list):
        matches = []
        for result in list:
            if sorted(result.casefold()) == sorted(self.word.casefold()) and result.casefold() != self.word.casefold():
                matches.append(result) 
        return matches
    
# .lower and .casefold same but not with islower