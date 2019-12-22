# pylint: disable=missing-docstring, bare-except, protected-access, invalid-name
import pandas as pd
from lecture import Lecture


class Teacher:
    """
    Содержит в себе преподавателя
    """

    _df = pd.DataFrame()
    _dates = []
    _pairs = {}

    @staticmethod
    def df_parser(teacher_df):
        """
        Парсит входные данные из листа с занятиями
        преподавателя и возвращает объект типа Преподаватель
        :param: pd.DataFrame
        :return: Teacher
        """
        teacher = Teacher()
        teacher._df = teacher_df
        teacher._dates = []
        teacher._pairs = {}

        months = ['сентября', 'октября', 'ноября',
                  'декабря', 'января', 'февраля',
                  'марта', 'апреля', 'мая',
                  'июня', 'июля', 'августа']

        for col_num in teacher._df.columns:

            dates = []
            selected_rows = []
            rows_num = len(teacher._df.index) + 1

            for row_num, row in teacher._df.iterrows():
                cell = row[col_num]
                try:
                    if cell.split(' ')[1] in months:
                        dates.append(cell)
                        selected_rows.append(row_num + 1)
                except:
                    pass

            teacher._dates += dates
            selected_rows.append(rows_num)

            for i, date in enumerate(dates):
                pairs_df = teacher._df[col_num][selected_rows[i]:selected_rows[i + 1] - 1]
                pairs = pairs_df.replace(pd.np.nan, '')
                teacher._pairs[date] = [Lecture.cell_parser(pair) for pair in pairs]

        for date in teacher._pairs:
            teacher._pairs[date] = Teacher.parse_pairs(teacher._pairs[date])
        return teacher

    @staticmethod
    def parse_pairs(lectures_list) -> list:
        """
        Получает лист преподавателей и их занятий и приводит к
        известному формату
        :param: list of Lectures
        :return: list
        """
        pairs = lectures_list[:]
        if len(pairs) == 5:
            pairs[2] = pairs[2] if pairs[2].get_full_value() else pairs[3]
            pairs[3] = pairs[4]
            pairs = pairs[:-1]
        if len(pairs) > 5:
            pairs[2] = pairs[2] if pairs[2].get_full_value() else pairs[3]
            pairs[3] = pairs[4] if pairs[4].get_full_value() else pairs[5]
            pairs = pairs[:4]
        return pairs

    def get_pairs_dict(self) -> dict:
        """
        Возвращает словарь со всеми парами преподавателя

        :return: dict
        """
        return self._pairs

    def get_dates_list(self) -> list:
        """
        Возвращает все даты с листа таблицы в формате листа
        :return: list
        """
        return self._dates
