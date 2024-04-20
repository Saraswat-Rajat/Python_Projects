# traesure map

list_1 = [' ', ' ', ' ']
list_2 = [' ', ' ', ' ']
list_3 = [' ', ' ', ' ']

map = [list_1, list_2, list_3]

position = input()

letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)

number_index = int(position[1]) - 1
map[number_index][letter_index] = 'X'


print(f'{list_1} \n {list_2} \n {list_3}')
