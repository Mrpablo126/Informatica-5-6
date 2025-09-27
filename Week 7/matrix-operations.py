def main():
    matrix = [[1,4,7,1],[3,2,5,8],[5,3,6,9],[2,4,7,10]]
    for row in matrix:
        print(f"{row}")
    sum_of_row(matrix)
    sum_of_column(matrix)
    print("")
    change_value

def sum_of_row(matrix, row_number):
    row_number  = int(input("Select the row"))
    row = matrix [row_number]
    row_sum = 0
    for item in row:
        row_sum += item 
             
    print(row_sum)
    
def sum_of_column(matrix, column_number):
    column_sum = int(input("Enter a number: ")) 
    tilin = 0
    for row in matrix:
        tilin += row[column_sum]
    print(column_sum)
    
def change_value(matrix, row_number, column_number, new_value):
    row_number = int(input("Enter a row number: "))
    column_number = int(input("Enter a column number: "))
    new_value = int(input("Enter a new value: "))
    matrix[row_number][column_number] = new_value
    for row in matrix:
        print(f"{row}") 

main()
