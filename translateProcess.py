import time

from requests_html import AsyncHTMLSession
import asyncio

import jsonController
import wordController
import json
from classType import japanWords
import SQLController


def getLinkJisho(word):
    return f'https://jisho.org/search/{word}%20%23kanji'


def getLinkMazii():
    return f'https://mazii.net/api/search'


async def getMazii(asyncSession, url, word):
    datas = {'dict': "javi", 'type': "kanji", 'query': f"{word}", 'page': 1}
    r = await asyncSession.post(url, data=datas)
    page = r.html.text
    try:
        b = json.loads(page)
        for i in b['results']:
            c = dict(i)
        return [c['mean'], c['detail'], c['on'], c['kun'], c['level']]
    except Exception as ex:
        print(ex.__class__.__name__)
        return ['err', 'err', 'err', 'err', 'err']


async def getJisho(asyncSession, url):
    r = await asyncSession.get(url)
    content = r.html

    return [findJishoContent(content, 'kanji-details__main-meanings'), findJishoContent(content, 'grade'),
            findJishoContent(content, '//*[@id="result_area"]/div/div[1]/div[1]/div/div[2]/div[1]', xpath=True),
            findJishoContent(content, '//*[@id="result_area"]/div/div[1]/div[1]/div/div[2]/div[2]/dl', xpath=True),
            findJishoContent(content, '//*[@id="result_area"]/div/div[1]/div[1]/div/div[2]/div[3]/dl', xpath=True)]


def findJishoContent(content, name, **kwargs):
    if kwargs.get('xpath'):
        try:
            return content.xpath(f'{name}')[0].text
        except Exception as ex:
            print(f'Warning: {ex.__class__.__name__}, {name}, in traslateProcess in findJishoContent [1].')
            return None
    else:
        try:
            return content.find(f'.{name}', first=True).text
        except Exception as ex:
            print(f'Warning: {ex.__class__.__name__}, {name}, in traslateProcess in findJishoContent [2].')
            return None


async def asyncWords(words, type):
    asyncSession = AsyncHTMLSession()
    if type == 'mazii':
        getMaziiTasks = (getMazii(asyncSession, getLinkMazii(), word) for word in words)
        return await asyncio.gather(*getMaziiTasks)
    if type == 'jisho':
        getJishoTasks = (getJisho(asyncSession, getLinkJisho(word)) for word in words)
        return await asyncio.gather(*getJishoTasks)


def asyncSegmentsSession(words, chunks, type):
    temp = []
    results = []
    counter = 0
    totalWords = 0
    for i in words:
        totalWords += len(i)
    wordList = wordController.splitString(words, chunks)
    for word in wordList:
        tmp = wordController.splitString(word, 1)
        counter += len(tmp)
        temp.append(asyncio.run(asyncWords(tmp, type)))
        print(f'searched {counter} out of {totalWords} in {type}')
        jsonController.setCountersToFile(counter, totalWords, type)
    for result in temp:
        for innerResult in result:
            results.append(innerResult)
    return results


def jointMultipleSegments(kanjiList, mazii=[], jisho=[]):
    results = []
    for i in range(len(kanjiList)):
        results.append(jointSegments(kanjiList[i], mazii[i], jisho[i]))
    return results


def jointSegments(kanji, mazii: list, jisho: list):
    return japanWords(kanji=kanji, english=jisho[0], mean=mazii[0], vietnamese=mazii[1], on=mazii[2], kun=mazii[3],
                      strokes=jisho[2], radicals=jisho[3], parts=jisho[4], level=mazii[4], taught=jisho[1])


def appendTraslated(words, chunks=45):
    jsonController.setCountersToFile(0, len(words), 'mazii')
    jsonController.setCountersToFile(0, len(words), 'jisho')
    if words == '':
        pass
    else:
        maziiArr = asyncSegmentsSession(words, chunks, 'mazii')
        jishoArr = asyncSegmentsSession(words, chunks, 'jisho')
        objs = jointMultipleSegments(words, maziiArr, jishoArr)
        SQLController.appendMultiple(objs)


def listToString(items):
    return ''.join([str(item) for item in items])


if __name__ == '__main__':
    rawWords = wordController.readFile('.\\Input\\', folder=True)
    rawWords = wordController.deleteDuplicate(rawWords, wordController.filteredWords(), database=False)
    print(rawWords)
    appendTraslated(rawWords)
    # print(rawWords)
    # 0
    # 933766711 0914800347
    # print(rawWords)