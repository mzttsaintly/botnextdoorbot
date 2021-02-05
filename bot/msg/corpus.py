# coding=utf-8

import os
import re
from mist.csv_reader import CsvReader
from mist import logger as log
from random import randint


class Corpus:
    corpus = {}

    def __init__(self):
        csv_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../res/corpus/aqiang.csv")
        self.corpus["aqiang"] = CsvReader().read_as_dict(csv_path)

    def compile(self, msg: str, sources=None):
        if sources is None:
            sources = self.corpus.keys()
        log.i("sources: ", sources)
        for key in sources:
            for question in self.corpus[key]:
                if re.search(question[0], msg):
                    log.i("question match: ", question)
                    return self.getAnswer(question)

    def getAnswer(self, question: list):
        index = question[randint(1, len(question) - 1)]
        log.i("get answer index: %d" % index)
        return CsvReader().read_answer(index)


if __name__ == "__main__":
    corpus = Corpus()
    print(corpus.compile("既然你诚心诚意的发问了"))
