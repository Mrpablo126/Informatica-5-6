def sum_of_row(matrix, row_number):
    return sum(matrix[row_number])
    # row = matrix [row_number]
    # row_sum = 0
    # for item in row:
    #     #row_sum = row_sum + item #linea 5 y 6 es lo mismo
    #     row_sum += item          

    return row_sum

def sum_of_column(matrix, column_number: int):
    column_sum = 0
    for row in matrix:
        column_sum = column_sum + row[column_number]
    
    return column_sum

def change_value(matrix, row_number, column_number, new_value):
    row = matrix([row_number])
    row[column_number] = new_value
    m = [[4,2,3,2], [9,1,12,11], [7,8,9,5], [2,9,15,1]]
    print(m)
change_value(m,2,3,1000)



    

