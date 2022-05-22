def find_word_concatenation(str1, words):
    n = len(str1)
    count = len(words)
    word_len = len(words[0])
    words_freq = {}
    res = []

    for word in words:
        if word not in words_freq:
            words_freq[word] = 0
        words_freq[word] += 1

    last_index = n - (word_len * count) + 1

    for i in range(last_index):
        words_seen = {}
        for j in range(count):
            next_word_index = i + j*word_len
            word = str1[next_word_index: next_word_index+word_len]
            if word not in words_freq:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > words_freq.get(word, 0):
                break

            if j+1 == count:
                res.append(i)

    return res
