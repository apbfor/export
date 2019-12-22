# pylint: disable=missing-docstring, invalid-name, protected-access, line-too-long


COMP_CLASSES = ['122', '103', '113', '124', '20_УНЦ', '17_УНЦ', 'КВАНТ-КК']


class Lecture:
    """
    Класс содержит описание учебного занятия
    """
    _full_value = ''
    _number = ''
    _name = ''
    _in_comp_class = False
    _groups = []
    _type = ''
    _classroom = ''

    def __eq__(self, other):
        return self._full_value == other._full_value if isinstance(other, Lecture) else False

    def to_list(self, teacher_name) -> list:
        """
        Представляет пару как лист
        :param teacher_name: Имя преподавателя в виде строки
        :return: лист, содержащий текущую пару
        """
        return [teacher_name, self._groups, self._classroom, self._in_comp_class] if self._full_value else []
    @staticmethod
    def cell_parser(pair_str):
        """
        Парсит входящие значения из ячеек таблицы, возвращает объект типа Lecture
        :param pair_str: строковое значение из таблицы
        :return: Объект типа Lecture
        """
        lecture = Lecture()
        lecture._full_value = pair_str

        if len(pair_str.split(':')) != 2:  # на случай, если в одно занятие несколько пар
            return lecture

        lecture._name = pair_str.split(':')[0]
        buf = pair_str.split(':')[1]
        buf_list = pair_str.split('\n')
        lecture._classroom = buf_list[-2].split(' ')[-1]
        lecture._in_comp_class = lecture._classroom in COMP_CLASSES
        buf = buf.split('-')
        buf_type = buf[0]
        buf_number = buf[1]
        buf = buf_list[-1].split('гр. ')[1]
        lecture._groups = buf.split('; ')
        lecture._type = buf_type.split('\n')[-1].split(' ')[-1]
        lecture._number = buf_number.split('\n')[0].split(' ')[0]

        return lecture

    def get_full_value(self) -> str:
        return self._full_value

    def get_name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return self._type

    def get_lecture_number(self) -> str:
        return self._number

    def is_in_computer_class(self) -> bool:
        return self._in_comp_class

    def get_classroom(self) -> str:
        return self._classroom

    def get_groups(self) -> list:
        return self._groups
