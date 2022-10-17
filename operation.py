#calculate and add to table total points of players.
def total(chess_table):
    order = 0
    for i in chess_table.table_data:
        total = 0.0
        for j in range(chess_table.number_of_players):
            if i[str(j + 1)] == '1':
                total += 1
            elif i[str(j + 1)] == '0.5':
                total += 0.5
        i['total'] = str(total)
        order += 1
# data of old order need to find result in table after convertion.
        i['old_order'] = order
    chess_table.header.append('total')
# 'old_order' not add to header of table because it need only for convert table, not need wtite it in file.
    return chess_table

# calculate and add to table berger coеfficient for all players.
def berger(chess_table):
    chess_table = total(chess_table)
    for i in range(chess_table.number_of_players):
        berger = 0
        for j in range(1, chess_table.number_of_players + 1):
            if chess_table.table_data[i][str(j)] == '*':
                continue
            else:
                berger += float(chess_table.table_data[i][str(j)]) * float(chess_table.table_data[j-1]['total'])
        chess_table.table_data[i]['berger'] = berger
    chess_table.header.append('berger')
    return chess_table

#sort and convert table to correspond total result and berger coefficient.
def converter(chess_table):
    from copy import deepcopy

    chess_table = berger(chess_table)
    data_old = deepcopy(chess_table.table_data)
    chess_table.table_data.sort(key = lambda x: x['berger'], reverse=True)
    chess_table.table_data.sort(key = lambda x: x['total'], reverse=True)
    data_new = deepcopy(chess_table.table_data)
    position = 0
    for i in chess_table.table_data:
        for j in range(1, chess_table.number_of_players + 1):
            i[str(j)] = data_old[i['old_order'] - 1][str(data_new[j - 1]['old_order'])]
        position += 1
        i['position'] = position
    chess_table.header.append('position')
    return chess_table