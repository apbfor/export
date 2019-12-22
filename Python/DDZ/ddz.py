# pylint: disable=missing-docstring, line-too-long, logging-not-lazy
import sys
from toJSON import JSONSerializer


def main():
    if len(sys.argv) < 3:
        print("Использование: python3 ddz.py filename.xlsx filename.json")
        sys.exit(1)

    input_name = sys.argv[1]
    output = open(sys.argv[2], 'w')

    JSONSerializer.serialize(excel_file=input_name).dump(
        file=output
    )
    print("Закончили парсинг из %s в %s" % (input_name, output.name))


if __name__ == '__main__':
    main()
