import sqlite3 as sql
import jsonController
from classType import japanWords


def connectDatabase():
    settings = jsonController.Settings()
    conn = sql.connect(settings.databaseLocation)
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE jpWords (id INTEGER PRIMARY KEY AUTOINCREMENT, kanji TEXT, means TEXT,\
                    englishMeanings TEXT, vietnameseMeanings TEXT, onReading TEXT, kunReadings TEXT, strokes TEXT,\
                     radicals TEXT, parts TEXT,level INT, taught TEXT)")
    except sql.OperationalError as ex:  # Check if table is already created
        print(f'{ex}, expected')
        pass

    return settings, conn, cur


settings, conn, cur = connectDatabase()


def appendMultiple(arr, update=False):
    temporary = deleteDuplicate(arr)
    temporary = multipleObjToArray(temporary)
    conn.executemany('REPLACE INTO jpWords(kanji, means, englishMeanings, vietnameseMeanings, onReading, kunReadings,\
                    strokes, radicals, parts, level, taught) VALUES(?,?,?,?,?,?,?,?,?,?,?)', temporary)
    conn.commit()
    # a = cur.execute("""SELECT EXISTS(SELECT 1 FROM jpWords WHERE japanWords=? LIMIT 1)""",(temporary[0][0], )).fetchone()[0]
    # print(a)


def updateDatabase(obj: japanWords):
    conn.execute(f"""UPDATE jpWords SET means = '{obj.mean}' , englishMeanings = '{obj.english}' ,
                            vietnameseMeanings = '{obj.vietnamese}' , onReading = '{obj.on}' , kunReadings = '{obj.kun}' , 
                            strokes = '{obj.strokes}' , radicals = '{obj.radicals}' , parts = '{obj.parts}' , level = '{obj.level}',
                            taught = '{obj.taught}' WHERE kanji = '{obj.kanji}'""")
    conn.commit()


def deleteDuplicate(arr):
    i = 0
    while i < len(arr):
        if checkExists('kanji', arr[i].kanji) == 1:
            arr.pop(i)
        else:
            i += 1
    return arr


def checkExists(type, word):
    return cur.execute(f"""SELECT EXISTS(SELECT 1 FROM jpWords WHERE {type}=? LIMIT 1)""", (word,)).fetchone()[0]


def multipleObjToArray(objs):
    temporary = []
    for i in range(len(objs)):
        temporary.append(objs[i].toArray())
    return temporary


def deleteIndex(kanji):
    conn.execute(f"""DELETE FROM jpWords WHERE kanji='{str(kanji)}'""")
    conn.commit()


def getWord(type, word):
    return cur.execute(f"""SELECT * FROM jpWords WHERE {type}=?""", (word)).fetchone()


def getAllWord(type, word):
    return cur.execute(f"""SELECT * FROM jpWords WHERE {type}=?""", (word)).fetchall()


def getSimilarWords(type, words):
    try:
        results = cur.execute(f"""SELECT * FROM jpWords WHERE {type} LIKE '%{words}%'""").fetchall()
        if len(results) == 0:
            return results
        else:
            return results
    except sql.OperationalError:
        print(f'Word {words} not found')


def databaseToObjects(words: list or tuple):
    try:
        if type(words[0]) is not list and type(words[0]) is not tuple:
            return japanWords(kanji=words[1], mean=words[2], english=words[3], vietnamese=words[4], on=words[5],
                              kun=words[6], strokes=words[7], radicals=words[8], parts=words[9], level=words[10],
                              taught=words[11])
        else:
            return [japanWords(kanji=word[1], mean=word[2], english=word[3], vietnamese=word[4], on=word[5],
                               kun=word[6], strokes=word[7], radicals=word[8], parts=word[9], level=word[10],
                               taught=word[11]) for word in words]

    except Exception as ex:
        return []


def removeObjectDuplicate(wordsList: list):
    seenKanji = []
    newList = []
    for word in wordsList:
        if word.kanji not in seenKanji:
            seenKanji.append(word.kanji)
            newList.append(word)
    return newList


def findObjectInDatabase(words, **kwargs):
    results = []
    if kwargs.get('absoluteSearch'):
        results.extend(databaseToObjects(getSimilarWords('kanji', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('means', f'{words.upper()}')))
        results.extend(databaseToObjects(getSimilarWords('level', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('englishMeanings', f'{words}')))
    else:
        results.extend(databaseToObjects(getSimilarWords('englishMeanings', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('vietnameseMeanings', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('kanji', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('means', f'{words.upper()}')))
        results.extend(databaseToObjects(getSimilarWords('level', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('onReading', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('kunReadings', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('radicals', f'{words}')))
        results.extend(databaseToObjects(getSimilarWords('parts', f'{words}')))
    return removeObjectDuplicate(results)


def getAllObjects():
    return databaseToObjects(cur.execute("SELECT * FROM jpWords").fetchall())


def getWordsObjects(words):
    results = []
    for word in words:
        results.append(databaseToObjects(getWord('kanji', word)))
    return results

if __name__ == "__main__":
    print(databaseToObjects(getWord('kanji', '愛')))
    pass
    # a = findObjectInDatabase('l')
    # for i in a:
    #     print(i.kanji)

    # pass
    # for i in c:
    #     for j in range(len(i)):
    #         print(i[j], j)
    # print(databaseToObjects(c))
    # print(removeObjectDuplicate(databaseToObjects(getSimilarWords('englishMeanings','l'))))
    # print(c)
    # print(databaseToObjects(getSimilarWords('englishMeanings', 'l')))
# print(getSimilarWords('englishMeanings','lo'))

# a = japanWords(kanji = 1,on = 2, level = 4, english = 5,vietnamese = 6, mean = 'a')
# print(a.toArray())
# b = japanWords(2,3,4,5)
# c = japanWords(5,6,7,8)
# ar = [a]
# appendMultiple(ar)
