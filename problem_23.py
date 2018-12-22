def add_word(trie, word, pos):
    if pos < len(word):
        if trie[ord(word[pos]) - ord('a')] == None:
            trie[ord(word[pos]) - ord('a')] = [None] * 26 
        add_word(trie[ord(word[pos]) - ord('a')], word, pos+1) 

def find(trie, word, pos):
    if pos == len(word):
        return True
    
    return False if trie[ord(word[pos]) - ord('a')] == None else find(trie[ord(word[pos]) - ord('a')], word, pos+1)     

def solve(original_trie, trie, word, start, end, sentence):
    if end != len(word) and start != len(word):
        if trie[end] == None:
            sentence.append(word[start:end]) 
            start = end
            solve(original_trie, original_trie, word, start, end, sentence) 
        else:
            solve(original_trie, trie[ord(word[end]) - ord('a')], word, start, end+1, sentence) 

trie = [None] * 26 

dictionary = input().split() 
code = input() 

for i in dictionary:
    add_word(trie, i, 0) 


res = []
solve(trie, trie, code, 0, 0, res) 

print("\n".join(res)) 