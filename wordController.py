import json

import SQLController as sqlcon
import jsonController
import os

settings = jsonController.Settings()


def filteredWords():
    try:
        with open(settings.filterPath, 'r', encoding='utf-8') as filter:
            return filter.read()
    except:
        with open(settings.filterPath, 'w', encoding='UTF-8') as filter:
            filter.write("""あいえうおやゆよかきくけこきゃきゅきょさしすせそしゃしゅしょたちつてとちゃちゅちょなにぬねのにゃにゅにょはひふ
            へほひゃひゅひをんがぎぐげょまみむめもみゃみゅみょやゆよらりるれろりゃりゅりょわゐゑごぎゃぎゅぎょざじずぜぞじゃじゅじょだぢづで
            どぢゃぢゅぢょばびぶべぼびゃびゅびょぱぴぷぺぽぴゃぴゅぴょアイウエオャュョカキクケコキャキュキョサシスセソシャシュショタチツテト
            チャチュチョナニヌネノニャニュニョハヒフヘホヒャヒュヒョマミムメモミャミュミョヤユヨラリルレロリャリュリョワヰヱヲンガギグゲゴギ
            ャギュギョザジズゼゾジャジュジョダヂヅデドヂャヂュヂョバビブベボビャビュビョパピプペポピャピュピョっ ? ？　! 1234567890  = _ # 
            ,:.();\ " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ …  「」ィェー々/[-]{}+<>
            ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂ ưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ'""")
        return filteredWords()


# def readFilterWords():
#     try:
#         with open(settings.filterPath, 'r', encoding='UTF-8') as f:
#             rawWords = f.read()
#         if rawWords == '':
#             with open(settings.filterPath, 'w', encoding='UTF-8') as f:
#                 f.write(filteredWords())
#                 rawWords = f.read()
#     except FileNotFoundError:
#         with open(settings.filterPath, 'w', encoding='UTF-8') as f:
#             f.write(filteredWords())
#         with open(settings.filterPath, 'r', encoding='UTF-8') as f:
#             rawWords = f.read()
#     return rawWords


def deleteDuplicate(file: str, filter: str, **kwargs) -> str:
    """
    kwargs:

    org:
    1: return unmodified file
    2: return filtered file without going through database

    database (bool): use database to delete duplicates
    """

    org: str
    if kwargs.get('org') == 1:
        org = str(file)
    if len(filter) != 0:
        for i in filter:
            file = file.replace(i, '')

    i = 0
    while i < len(file):
        if file.count(file[i]) > 1:
            file = file.replace(file[i], '', 1)
        if file.count(file[i]) < 1:
            raise Exception('There is something wrong')
        if file.count(file[i]) == 1:
            i += 1

    if kwargs.get('org') == 2:
        org = str(file)

    if kwargs.get('database'):
        i = 0
        while i < len(file):
            exist = sqlcon.checkExists('kanji', f'{file[i]}')
            if exist > 0:
                file = file.replace(file[i], '', 1)
            if exist == 0:
                i += 1

    if kwargs.get('org') != 0 and kwargs.get('org') is not None:
        return org, file
    else:
        return file


def readFile(*args, **kwargs) -> str:
    fileList = []
    rawWords = ''
    for arg in args:
        if kwargs.get('folder'):
            for root, dirs, files in os.walk(f"{arg}"):
                for file in files:
                    if file.endswith(".txt"):
                        fileList.append(os.path.join(root, file))
            for fileDir in fileList:
                with open(f'{fileDir}', 'r', encoding='UTF-8') as file:
                    rawWords = rawWords + file.read()
        else:
            try:
                filePaths = arg.split(', ')
                for filePath in filePaths:
                    with open(f'{filePath}', 'r', encoding='UTF-8') as file:
                        rawWords = rawWords + file.read()
            except FileNotFoundError:
                print(f'file {arg} not found.')
    return rawWords


def splitString(file, length=10):
    i = 0
    stringChunk = []
    lenFile = len(file)
    while i < lenFile:
        if i + length < lenFile:
            stringChunk.append(file[i:i + length])
            i += length
        else:
            stringChunk.append(file[i:lenFile])
            i += length
    return stringChunk

# if __name__ == '__main__':
#     setCountersInFile(1,2)


# def createJPObject(type, word):
#     word = sqlcon.getWord(f'{type}', f'{word}')
#     if word is None:
#         pass
#     else:
#         return japanWords(kanji=word[1], mean=word[2], english=word[3], vietnamese=word[4], on=word[5], kun=word[6],
#                           level=word[7])


# def createJPObjects(typeWords, words):
#     if type(words) == str:
#         words = splitString(words, 1)
#     if type(words) == list or type(words) == tuple:
#         return [createJPObject(f'{typeWords}', word) for word in words]
#     else:
#         raise TypeError(f'Expect list, string or tuple, not {type(words).__name__}')


# def findAndCreateObject(typeWords, words):
#     words = deleteDuplicate(words, filteredWords(), database=True, org=2)
#     translateProcess.appendTraslated(words[1])
#     words = createJPObjects(typeWords, words[0])
#     return words


# if __name__ == '__main__':
#     rawWords = readFile('.\\Input\\', folder=True)
#     rawWords = deleteDuplicate(rawWords, filteredWords(), database=True, org = 2)
#     a = (findAndCreateObject('kanji',f'{rawWords[0]}'))
#     print(a[0].toArray())
#     a[0].english = 'akisjdoas'
#     print(a[0].toArray())
