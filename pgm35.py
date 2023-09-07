def group_anagrams(words):
    anagram_groups = {}
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    
    return anagram_groups


word_list = ["listen", "silent", "hello", "world", "act", "cat", "god", "dog"]
anagram_dict = group_anagrams(word_list)

for key, value in anagram_dict.items():
    print(f"Anagrams of {', '.join(value)}: {key}")
