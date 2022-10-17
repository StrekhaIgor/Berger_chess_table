import in_out as i_o

# checking results in table. Return 'True' if all results are 1-0, 0-1 or draw.
def validation(chess_table):
    for i in range(chess_table.number_of_players):
        for j in range(1, chess_table.number_of_players + 1):
            if i + 1 != j:
                res_one = float(chess_table.table_data[i][str(j)])
                res_two = float(chess_table.table_data[j - 1][str(i + 1)])
                if res_one + res_two != 1.0 or res_one not in [0.0, 1.0, 0.5]:
                    return False
    return True

# compared all results in converted table with coresponding results in original table.
def proof(file_name):
    table_old = i_o.read_cvs(file_name)
    covert_name = file_name.strip('.csv') + '_converted.csv'
    table_conv = i_o.read_cvs(covert_name)
    # key_name is value from first column of original table. It using for find results of game in converted table
    key_name = table_old.header[0] 
    for one in range(table_old.number_of_players):
        for two in range(table_old.number_of_players):
            res_old = table_old.table_data[one][str(two + 1)]
            one_conv = list(filter(lambda x: x[key_name] == str(one + 1), table_conv.table_data))[0]['position']
            two_conv = list(filter(lambda x: x[key_name] == str(two + 1), table_conv.table_data))[0]['position']
            res_new = table_conv.table_data[int(one_conv) - 1][two_conv]
            if res_old != res_new:
                return False
    return True