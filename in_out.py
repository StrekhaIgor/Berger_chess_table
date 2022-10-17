from glob import glob
from collections import namedtuple


# return list of csv-file names, except already converted
def get_name():
    return [i for i in glob('*.csv') if not i.endswith('converted.csv')]


# find type delimiter, which is used in line of cvs-file
def find_delimiter(cvs_line):
    return max(['\t', ';', ','], key=lambda x: cvs_line.count(x))


# reading from cvs-file chess table and return named tuple 'chess_table', which is contened: number_of_players, header, table_data, file_name, delimiter. 
# table_data is list of dictioneries. Keys dictinaries are headers of table, values - data of each player
def read_cvs(file_name):
    with open(file_name, encoding='utf-8') as table:
        line = table.readline().strip()
        delimiter = find_delimiter(line)
        header = line.split(delimiter)
        number_of_players = max([int(i) for i in header if i.isdigit()])
        # need, because table may be contain 'trash' info such as data about arbiter
        table_data = []
        for _ in range(int(number_of_players)):
            if delimiter == ',':
                line_table = table.readline().strip().replace('"0,5"', '0.5')
            else:
                line_table = table.readline().strip().replace('0,5', '0.5')
            #line_table = line_table.replace('"0.5"', '0.5')
            table_data.append(dict(zip(header, line_table.split(delimiter))))
        header = header[:(header.index(str(number_of_players)) + 1)]
        table_info = namedtuple('table', 'number_of_players header table_data file_name delimiter')
        chess_table = table_info(number_of_players, header, table_data, file_name, delimiter)
    return chess_table


def write_cvs(chess_table):
    _, header, table_data, file_name, delimiter = chess_table
    new_name = file_name.rstrip('.csv') + '_converted.csv'
    with open(new_name, 'w', encoding='utf-8') as table:
        print(delimiter.join(header), file=table)
        for i in table_data:
            line = delimiter.join([str(i[j]) for j in header])
            print(line, file=table)