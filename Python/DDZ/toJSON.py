# pylint: disable=missing-docstring, invalid-name, protected-access
import json
from ExPars import ExcelParser
from teacher import Teacher


class JSONSerializer:

    _xl_file = None
    _dates = []
    _names = []
    _date_dict = {}
    _teachers_pairs_dict = {}

    @staticmethod
    def serialize(excel_file):
        jsonobj = JSONSerializer()

        jsonobj._xl_file = ExcelParser(excel_file)
        jsonobj._names = jsonobj._xl_file.get_teachers_list()
        jsonobj._teachers_pairs_dict = {}

        for teacher_name in jsonobj._names:
            df = jsonobj._xl_file.get_teacher_df(teacher_name)
            teacher = Teacher.df_parser(df)
            jsonobj._teachers_pairs_dict[teacher_name] = teacher.get_pairs_dict()
            jsonobj._dates += teacher.get_dates_list()

        for date in set(jsonobj._dates):
            jsonobj._date_dict[date] = {i: [] for i in range(1, 5)}

        for teacher_name in jsonobj._names:
            for date in jsonobj._teachers_pairs_dict[teacher_name]:
                for i, pair in enumerate(jsonobj._teachers_pairs_dict[teacher_name][date]):
                    pair_list = pair.to_list(teacher_name)
                    if pair_list:
                        jsonobj._date_dict[date][i + 1].append(pair_list)
        return jsonobj

    def dump(self, file):
        file.write(json.dumps(self._date_dict, indent=4, ensure_ascii=False))
