class japanWords:
    def __init__(self, **kwargs):
        """kanji: kanji word

        on : on reading;

        kun: kun reading;

        level: jlpt level;

        mean: Phiên âm

        english: english meaning;

        vietnamese: vietnamese meaning;
        """
        self.kwargs = kwargs
        self.kanji = self.assignValue('kanji')
        self.mean = self.assignValue('mean')
        self.on = self.assignValue('on')
        self.kun = self.assignValue('kun')
        self.level = self.assignValue('level')
        self.english = self.assignValue('english')
        self.vietnamese = self.assignValue('vietnamese')
        self.strokes = self.assignValue('strokes')
        self.radicals = self.assignValue('radicals')
        self.parts = self.assignValue('parts')
        self.taught = self.assignValue('taught')

    def toDict(self):
        return {'japanWords': self.kanji, 'englishMeanings': self.english,
                'vietnameseMeanings': self.vietnamese, 'on': self.on, 'kun': self.kun, 'level': self.level}

    def toArray(self):
        return [self.kanji, self.mean, self.english, self.vietnamese, self.on, self.kun,
                self.strokes, self.radicals, self.parts, self.level, self.taught]

    def assignValue(self, typeValue):
        try:
            return self.kwargs.get(typeValue)
        except Exception as ex:
            return ''


class japanWordRandom(japanWords):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':
    a = japanWordRandom(kun='asbcnujk')
    type = 'kun'
    print(getattr(a, type))
