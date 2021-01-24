# coding=utf-8

import csv
import pandas as pd
import numpy as np
import os


class CsvReader:

    def isEmpty(self, msg):
        return msg != ""

    def read_as_dict(self, path: str):
        csv_file = csv.reader(open(path))
        result = []
        for line in csv_file:
            line = [int(item) if item.isnumeric() else item for item in line]
            result.append(list(filter(self.isEmpty, line)))
        return result

    def read_answer(self, ans_index: int):
        path = os.path.abspath(
            os.path.dirname(os.path.abspath(__file__))
            + os.path.sep + "/../../res/corpus/answers.csv"
        )
        csv_file = csv.reader(open(path))
        for index, line in enumerate(csv_file):
            if index == ans_index:
                return line[0]
        return None


if __name__ == "__main__":
    csv_path = os.path.abspath(
        os.path.dirname(os.path.abspath(__file__))
        + os.path.sep + "/../../res/corpus/aqiang.csv"
    )
    print(CsvReader().read_as_dict(csv_path))
