my_list = [5, 2, 3, 1, 4]
greatest = max(my_list)
print("The greatest number in the list is:",greatest)

smallest = min(my_list)
print("The smallest number in the list is:",smallest)

list_sum = sum(my_list)
print("The sum of all numbers in the list is:",list_sum)

list_length = len(my_list)
print("This list has ", list_length, "elements.")

in_order = sorted(my_list)
print(in_order)

def filter_price(price):
    if (price >= 400):
        return True
    else:
        return False

item_price = [230, 400, 450, 350, 370]
filtered_price = filter(filter_price, item_price)
print(list(filtered_price))

