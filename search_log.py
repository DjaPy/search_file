import fnmatch
import os
import re


def search_wildcard(list_wildcards, path):
    list_files = []

    for wildcard in list_wildcards:
        for file in os.listdir(path):
            if fnmatch.fnmatch(file, wildcard):
                list_files.append(file)
    return list_files


# def get_list_of_string(list_files):
#     dict_line = {}
#     number_line = 0
#     for file in list_files:
#         file_path = os.path.join(path, file)
#         data = open(file_path, 'r')
#         for line in data:
#             number_line += 1
#             dict_line('number_line') =    return dict_line


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
    list_slice_of_line = []
    for index in list_index:
        range_lines = list_line[(index - 101):(index + 100)]
        slice_of_line = ''.join(range_lines)
        list_slice_of_line.append(slice_of_line)
    return list_slice_of_line


def writing_to_file(list_slice_of_line):
    file_write = open(filename, 'w', encoding='utf-8')
    for part_of_log in list_slice_of_line:
        file_write.write(part_of_log+'\n')
    file_write.close()


if __name__ == '__main__':
    path = input('Введите путь к каталогу для поиска: ')
    list_wildcards = [wildcard_file for wildcard_file in input('Введите маску файла(ов) через проблел: ').split()]
    id_pattern = input('Введите числовой идентификатор лога: ')
    path_write = input('Введите путь для записи файла: ')
    filename = os.path.join(path_write, id_pattern + '.txt')
    # print(search_wildcard(list_wildcards, path))

    list_files = search_wildcard(list_wildcards, path)
    # print(search_by_ID(list_files, id_pattern))

    list_index, list_line = search_by_ID(list_files, id_pattern)
    list_slice_of_line = to_range_of_lines(list_index, list_line)
    writing_to_file(list_slice_of_line)



