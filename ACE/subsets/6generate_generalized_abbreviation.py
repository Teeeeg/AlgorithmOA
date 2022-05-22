class AbbreviatedWord:
    def __init__(self, string, index, count) -> None:
        self.string = string
        self.index = index
        self.count = count


def generate_generalized_abbreviation(word):
    n = len(word)
    res = []
    queue = []
    queue.append(AbbreviatedWord(list(), 0, 0))

    while queue:
        abWord = queue.pop(0)
        if abWord.index == n:
            if abWord.count != 0:
                abWord.string.append(str(abWord.count))
            res.append(''.join(abWord.string))

        else:
            # 进行缩略，即递增count和index
            queue.append(AbbreviatedWord(
                list(abWord.string), abWord.index+1, abWord.count+1))
            # 记录递增
            if abWord.count != 0:
                abWord.string.append(str(abWord.count))

            # 从改单词处进行缩略
            newWord = abWord.string
            newWord.append(word[abWord.index])
            queue.append(AbbreviatedWord(newWord, abWord.index+1, 0))

    return res

# Time O(n*2^n)
# Space O(n*2^n)



def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
