import os

import SQLController as sqlcon
import jsonController

settings = jsonController.Settings()


def filteredWords():
    try:
        with open(settings.filterPath, 'r', encoding='utf-8') as filter:
            return filter.read()
    except:
        with open(settings.filterPath, 'w', encoding='UTF-8') as filter:
            filter.write(FILTERED_TEXT)
        return filteredWords()


FILTERED_TEXT = """。『』「」々、　"""

CHINESE_REPLACE = {'⼀': '一', '⼆': '二', '⼈': '人', '⼄': '乙', '丨': '丨', '⼃': '丿', '⼅': '亅', '⼇': '亠', '⼉': '儿',
                   '⼊': '入',
                   '⼋': '八', '⼌': '冂', '⼍': '冖', '⼎': '冫', '⼏': '几', '⼐': '凵', '⼑': '刀', '⼒': '力',
                   '⼓': '勹', '⼔': '匕', '⼕': '匚', '⼖': '匸', '⼗': '十', '⼘': '卜', '⼙': '卩', '⼚': '厂',
                   '⼛': '厶', '⼜': '又', '⼝': '口', '⼞': '囗', '⼟': '土', '⼠': '士', '⼡': '夂', '⼢': '夊',
                   '⼣': '夕', '⼤': '大', '⼥': '女', '⼦': '子', '⼧': '宀', '⼨': '寸', '⼩': '小',
                   '⼪': '尢', '⼫': '尸', '⼬': '屮', '⼭': '山', '⼮': '巛', '⼯': '工', '⼰': '己', '⼱': '巾', '⼲': '干',
                   '⼳': '幺', '⼴': '广', '⼵': '廴', '⼶': '廾', '⼷': '弋', '⼸': '弓', '⼹': '彐', '⼺': '彡', '⼻': '彳',
                   '⼼': '心', '⼽': '戈', '⼾': '戸', '⼿': '手', '⽀': '支', '⽁': '攴', '⽂': '文', '⽃': '斗',
                   '⽄': '斤', '⽅': '方', '⽆': '无', '⽇': '日', '⽈': '曰', '⽉': '月', '⽊': '木', '⽋': '欠',
                   '⽌': '止', '⽍': '歹', '⽎': '殳', '⽏': '毋', '⽐': '比', '⽑': '毛', '⽒': '氏', '⽓': '气', '⽔': '水',
                   '⽕': '火', '⽖': '爪', '⽗': '父', '⽘': '爻', '⽙': '爿', '⽚': '片', '⽛': '牙', '⽜': '牛',
                   '⽝': '犬', '⽞': '玄', '⽟': '玉', '⽠': '瓜', '⽡': '瓦', '⽢': '甘', '⽣': '生',
                   '⽤': '用', '⽥': '田', '⽦': '疋', '⽧': '疒', '⽨': '癶', '⽩': '白', '⽪': '皮',
                   '⽫': '皿', '⽬': '目', '⽭': '矛', '⽮': '矢', '⽯': '石', '⽰': '示', '⽱': '禸', '⽲': '禾',
                   '⽳': '穴', '⽴': '立', '⽵': '竹', '⽶': '米', '⽷': '糸', '⽸': '缶', '⽹': '网', '⽺': '羊',
                   '⽻': '羽', '⽼': '老', '⽽': '而', '⽾': '耒', '⽿': '耳', '⾀': '聿', '⾁': '肉', '⾂': '臣',
                   '⾃': '自', '⾄': '至', '⾅': '臼', '⾆': '舌', '⾇': '舛', '⾈': '舟', '⾉': '艮', '⾊': '色',
                   '⾋': '艸', '⾌': '虍', '⾍': '虫', '⾎': '血', '⾏': '行', '⾐': '衣', '⾑': '襾', '⾒': '見',
                   '⾓': '角', '⾔': '言', '⾕': '谷', '⾖': '豆', '⾗': '家', '⾘': '豸', '⾙': '貝', '⾚': '赤',
                   '⾛': '走', '⾜': '足', '⾝': '身', '⾞': '車', '⾟': '辛', '⾠': '辰', '⾡': '辵', '⾢': '邑',
                   '⾣': '酉', '⾤': '釆', '⾥': '里', '⾦': '金', '⾧': '長', '⾨': '門', '⾩': '阜',
                   '⾪': '隶', '⾫': '隹', '⾬': '雨', '⾭': '靑', '⾮': '非', '⾯': '面', '⾰': '革', '⾱': '韋',
                   '⾲': '韭', '⾳': '音', '⾴': '頁', '⾵': '風', '⾶': '飛', '⾷': '食', '⾸': '首', '⾹': '香',
                   '⾺': '馬', '⾻': '骨', '⾼': '高', '⾽': '髟', '⾾': '鬥', '⾿': '鬯', '⿀': '鬲', '⿁': '鬼',
                   '⿂': '魚', '⿃': '鳥', '⿄': '鹵', '⿅': '鹿', '⿆': '麥', '⿇': '麻', '⿈': '黃',
                   '⿉': '黍', '⿊': '黒', '⿋': '黹', '⿌': '黽', '⿍': '鼎', '⿎': '鼓', '⿏': '鼠', '⿐': '鼻',
                   '⿑': '齊', '⿒': '歯', '⿓': '龍', '⿔': '龜', '⿕': '龠'}


def deleteDuplicate(file: str, filtered: str, **kwargs):
    """
    kwargs:

    org:
    1: return unmodified file
    2: return filtered file without going through database

    database (bool): use database to delete duplicates
    """

    org = ''
    stringArr = []
    if kwargs.get('org') == 1:
        org = str(file)

    if len(filtered) != 0:
        for text in file:
            if ("\u2E80" <= text <= "\u2EFF") or ("\u2F00" <= text <= "\u2FDF") or ("\u3000" <= text <= "\u303f") \
                    or ("\u31C0" <= text <= "\u31ef") or ("\u3400" <= text <= "\u4dbf") or (
                    "\u4e00" <= text <= "\u9fff") \
                    or ("\uf900" <= text <= "\ufaff"):
                stringArr.append(text)
        file = ''.join(stringArr)
        for i in filtered:
            file = file.replace(i, '')
    print(f'{file=}')
    file = chineseToKanji(file)

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


def chineseToKanji(words):
    for word, replacement in CHINESE_REPLACE.items():
        words = words.replace(word, replacement)
    return words


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
#         return JapanWords(kanji=word[1], mean=word[2], english=word[3], vietnamese=word[4], on=word[5], kun=word[6],
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
