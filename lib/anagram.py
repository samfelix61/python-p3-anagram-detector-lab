# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        sorted_word = sorted(self.word)
        matches = [anagram for anagram in possible_anagrams if sorted(anagram) == sorted_word]
        return matches

# Example usage:
anagram_finder = Anagram('listen')
result = anagram_finder.match(['enlists', 'google', 'inlets', 'banana'])
print(result)  # Output: ['inlets']
