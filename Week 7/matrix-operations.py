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

number = int(input("Select a number:"))

m = [[4,2,3,2], [9,1,12,11], [7,8,9,5], [2,9,15,1]]
my_sum = sum_of_column(m,2)
print(my_sum)
m[0][3]= number
print(m)

print(sum_of_column(m,1))

