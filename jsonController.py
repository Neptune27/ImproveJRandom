import json
import traceback


class Settings:
    def __init__(self):
        try:
            self.var = {}
            self.jsonPath = '.\\settings.json'
            with open(self.jsonPath, 'r', encoding='UTF-8') as f:
                rawData = f.read()
            self.var = json.loads(rawData)
            self.databaseLocation = self.var["databaseLocation"]
            self.inputPath = self.var["inputPath"]
            self.filterPath = self.var["filterPath"]
            self.isFolder = self.var["isFolder"]
            self.assignVariable()
        except Exception:
            self.setDefaultSettings()
            print(traceback.format_exc())
            self.assignVariable()

    def setDefaultSettings(self):
        self.writeToJson("databaseLocation", '.\\Data\\defaultDatabase.db', self.jsonPath)
        self.writeToJson("inputPath", '.\\Input\\', self.jsonPath)
        self.writeToJson("filterPath", '.\\Data\\filterFile.txt', self.jsonPath)
        self.writeToJson("isFolder", True, self.jsonPath)
        self.assignVariable()

    def writeToJson(self, var, text, path):
        with open(f'{path}', 'w', encoding='UTF-8') as f:
            self.var[f'{var}'] = text
            f.write(json.dumps(self.var, indent=4, ensure_ascii=False))

    def assignVariable(self):
        try:
            with open(self.jsonPath, 'r', encoding='UTF-8') as f:
                rawData = f.read()
            self.var = json.loads(rawData)
            self.databaseLocation = self.var["databaseLocation"]
            self.inputPath = self.var["inputPath"]
            self.filterPath = self.var["filterPath"]
            self.isFolder = self.var["isFolder"]
        except Exception as ex:
            self.setDefaultSettings()

    def commitToFile(self):
        try:
            self.writeToJson("databaseLocation", self.databaseLocation, self.jsonPath)
            self.writeToJson("inputPath", self.inputPath, self.jsonPath)
            self.writeToJson("filterPath", self.filterPath, self.jsonPath)
            self.writeToJson("isFolder", self.isFolder, self.jsonPath)
            self.assignVariable()
        except TypeError as te:
            print(te)


def setCountersToFile(counter: int, totals: int, type: str) -> None:
    try:
        with open('./Data/counter.json', 'r', encoding='UTF-8') as counterfile:
            var = json.loads(counterfile.read())
        with open('./Data/counter.json', 'w', encoding='UTF-8') as counterfile:
            if type == 'mazii':
                var["maziiCounter"] = counter
                var["maziiTotal"] = totals
            elif type == 'jisho':
                var['jishoCounter'] = counter
                var['jishoTotal'] = totals
            counterfile.write(json.dumps(var, indent=4, ensure_ascii=False))
        print(var)
    except json.decoder.JSONDecodeError:
        with open('./Data/counter.json', 'w', encoding='UTF-8') as counterfile:
            var = {'maziiCounter': 0, 'maziiTotal': 0, 'jishoCounter': 0, 'jishoTotal': 0}
            counterfile.write(json.dumps(var, indent=4, ensure_ascii=False))
        setCountersToFile(counter, totals, type)


def setTypeToFile(questionType, answerType, len=0):
    try:
        with open('./Data/questionType.json', 'r', encoding='UTF-8') as questionFile:
            var = json.loads(questionFile.read())
        with open('./Data/questionType.json', 'w', encoding='UTF-8') as questionFile:
            var['questionType'] = questionType
            var['answerType'] = answerType
            var['len'] = len
            questionFile.write(json.dumps(var))
    except Exception as ex:
        print(ex, 'setTypeToFile')
        with open('./Data/questionType.json', 'w', encoding='UTF-8') as counterfile:
            counterfile.write(json.dumps({'questionType': 'kanji', 'answerType': 'english', 'len': 0}))
