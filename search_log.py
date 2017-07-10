import fnmatch
import os
import re
from argparse import ArgumentParser


def get_parser_of_command_line():
    parser = ArgumentParser(description=
                            'search by mask and ID in the logs')
    parser.add_argument('path_for_search',
                        help='Directory path', type=str)
    parser.add_argument('-w', '--wildcard', nargs='?', action='append',
                        help='Wildcard for search log', default=None,
                        type=str)
    parser.add_argument('-i', '--id', nargs='?',
                        help='ID pattern for search', default=None,
                        type=str)
    parser.add_argument('-o', '--output', nargs='?',
                        help='The path to write the file with the search results',
                        default=None, type=str)
    return parser.parse_args()


# def enter_data():
#     pass


def search_wildcard(list_wildcards, path):
    list_files = []

    for wildcard in list_wildcards:
        for file in os.listdir(path):
            if fnmatch.fnmatch(file, wildcard):
                if file not in list_files:
                    list_files.append(file)
    return list_files


def search_by_ID(list_files, id_pattern):
    list_index = []
    number_line = 0
    list_lines = []

    for file in list_files:
        file_path = os.path.join(path, file)
        data = open(file_path, 'r')
        for line in data:
            number_line += 1
            list_lines.append(line)
            if re.findall(id_pattern, line):
                list_index.append(number_line)
    return list_index, list_lines


def to_range_of_lines(list_index, list_line):
    min_range = 100
    max_range = 100
    list_slice_of_line = []
    for index in list_index:
        range_lines = list_line[(index - min_range):(index + max_range)]
        slice_of_line = ''.join(range_lines)
        list_slice_of_line.append(slice_of_line)
    return list_slice_of_line


def writing_to_file(list_slice_of_line, filename):
    file_write = open(filename, 'w', encoding='utf-8')
    for part_of_log in list_slice_of_line:
        file_write.write(part_of_log+'\n')
    file_write.close()


if __name__ == '__main__':
    # path = input('Введите путь к каталогу для поиска: ')
    # list_wildcards = [wildcard_file for wildcard_file in
    #                   input('Введите маску файла(ов) через пробел: ').split()]
    # id_pattern = input('Введите идентификатор лога: ')
    # path_write = input('Введите путь для записи файла: ')
    search_settings = get_parser_of_command_line()
    path = search_settings.path_for_search
    list_wildcards = [wildcard for wildcard in search_settings.wildcard]
    id_pattern = search_settings.id
    path_write = search_settings.output
    filename = os.path.join(path_write, id_pattern + '.txt')
    print(search_wildcard(list_wildcards, path))

    list_files = search_wildcard(list_wildcards, path)
    # print(search_by_ID(list_files, id_pattern))

    list_index, list_line = search_by_ID(list_files, id_pattern)
    list_slice_of_line = to_range_of_lines(list_index, list_line)
    writing_to_file(list_slice_of_line, filename)