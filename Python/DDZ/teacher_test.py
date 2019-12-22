# pylint: disable=missing-docstring, line-too-long, invalid-name
import unittest
import pandas as pd
from lecture import Lecture
from teacher import Teacher


class TestTeacher(unittest.TestCase):

    init_dataframes = [
        pd.DataFrame({
            'Unnamed: 2': {
                0: '11 сентября',
                1: pd.np.nan,
                2: pd.np.nan,
                3: 'Безопасность ОС:\nПЗ-15 ауд. 122\nгр. 7334',
                4: pd.np.nan,
                5: pd.np.nan
            }
        }),
        pd.DataFrame({
            '30 сентября': {
                0: '02 октября',
                1: pd.np.nan,
                2: pd.np.nan,
                3: 'Безопасность ОС: \nлаб.раб-1 ауд. 122\nгр. 7334',
                4: pd.np.nan,
                5: 'Безопасность ОС: \nсем.-1 ауд. 209\nгр. 7334'
            }
        }),
        pd.DataFrame({
            '04 ноября': {
                0: '06 ноября',
                1: pd.np.nan,
                2: pd.np.nan,
                3: pd.np.nan,
                4: pd.np.nan,
                5: pd.np.nan,
            }
        })
    ]

    def test_get_pairs_dict(self):
        pairs_list = [
            {
                '11 сентября': [
                    Lecture.cell_parser(''),
                    Lecture.cell_parser(''),
                    Lecture.cell_parser('Безопасность ОС:\nПЗ-15 ауд. 122\nгр. 7334'),
                    Lecture.cell_parser(''),
                ]
            },
            {
                '02 октября': [
                    Lecture.cell_parser(''),
                    Lecture.cell_parser(''),
                    Lecture.cell_parser('Безопасность ОС: \nлаб.раб-1 ауд. 122\nгр. 7334'),
                    Lecture.cell_parser('Безопасность ОС: \nсем.-1 ауд. 209\nгр. 7334'),
                ]
            },
            {
                '06 ноября': [
                    Lecture.cell_parser(''),
                    Lecture.cell_parser(''),
                    Lecture.cell_parser(''),
                    Lecture.cell_parser(''),
                ]
            }
        ]
        for (pairs, df) in zip(pairs_list, self.init_dataframes):
            teacher = Teacher.df_parser(df)
            self.assertEqual(pairs, teacher.get_pairs_dict())

    def test_get_dates_list(self):
        lists = [['11 сентября'], ['02 октября'], ['06 ноября']]
        for (l, df) in zip(lists, self.init_dataframes):
            teacher = Teacher.df_parser(df)
            self.assertEqual(l, teacher.get_dates_list())
