import berger_functions.in_out as i_o
import berger_functions.operation as oper
import berger_functions.my_test as test


for file_name in i_o.get_name():
    print(file_name)
    new_table = i_o.read_cvs(file_name)
    if test.validation(new_table):
        print('Данные таблицы корректны')
    else:
        print('Данные таблицы некорректны. Проверьте правильность результатов.')
        continue
    table_conv = oper.converter(new_table)
    i_o.write_cvs(table_conv)
    if test.proof(file_name):
        print('Таблица преобразована верно')
    else:
        print('Ошибка при преобразовании таблицы. Проверьте правильльность программы или исходного файла.')
if i_o.get_name() == []:
    print('Не найдены файлы для преобразования. Добавьте cvs-таблицу в папку с файлом "chess_table.py"')