# pylint: disable=missing-docstring, invalid-name
import pandas as pd


class ExcelParser:

    def __init__(self, excel_file):
        self._xl = pd.ExcelFile(excel_file)
        self._teachers_list = self._xl.sheet_names

    def get_teachers_list(self):
        return self._teachers_list

    def get_teacher_df(self, teacher_name):
        if teacher_name not in self._teachers_list:
            raise Exception('No such teacher: {}'.format(teacher_name))
        return self._xl.parse(teacher_name, header=None)
