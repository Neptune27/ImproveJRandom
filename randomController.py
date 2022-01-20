import random
import jsonController
import SQLController
import wordController
from classType import japanWords


def randomWordInWordList(wordList: list, **kwargs) -> list:
    randomList = []
    wordListToChoose = []
    if kwargs.get('len') and kwargs.get('len') != 0:
        wordListToChoose = random.sample(wordList, k=kwargs.get('len'))
    else:
        wordListToChoose = wordList
    for i in wordListToChoose:
        randomElement = []
        randomElement.append(i)
        while len(randomElement) < 4:
            randomWord = random.choices(wordList)
            if randomWord[0].kanji != i.kanji:
                randomElement.extend(randomWord)
        random.shuffle(randomElement)
        randomList.append(randomElement)
        # print(randomList)
    return wordListToChoose, randomList


if __name__ == '__main__':

    wordlist = SQLController.getAllObjects()

    a, b = randomWordInWordList(wordlist, len=4)
    # print(a)
    # b = [i.kanji for i in wordlist]
    # print(b)
    a = [i.kanji for i in a]
    print(a)

    for i in b:
        for j in i:
            print(j.kanji)
        print('\n')

    c = [i for i in range(len(a))]
    print(c)
    c[0] = b[0][2]
    print(c)
