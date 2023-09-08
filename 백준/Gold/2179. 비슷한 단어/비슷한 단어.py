def find_similar_words(words):
    max_length = 0
    similar_pair = ('', '')
    
    prefix_map = {}
    
    for word in words:
        current_prefix = ''
        for letter in word:
            current_prefix += letter
            if current_prefix in prefix_map:
                prefix_map[current_prefix].append(word)
            else:
                prefix_map[current_prefix] = [word]
    
    for word in words:
        current_prefix = ''
        for letter in word:
            current_prefix += letter
            if len(prefix_map[current_prefix]) > 1:
                length = len(current_prefix)
                if length > max_length:
                    max_length = length
                    similar_pair = (word, prefix_map[current_prefix][1])
    
    return similar_pair

# 입력 받기
N = int(input())
words = []
for _ in range(N):
    word = input()
    words.append(word)

# 가장 비슷한 두 단어 찾기
similar_words = find_similar_words(words)

# 결과 출력
print(similar_words[0])
print(similar_words[1])
