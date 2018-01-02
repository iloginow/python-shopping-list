my_list = []

while 'DONE' not in my_list:
    my_list.append(input('Add to the list: '))

my_list.remove('DONE')

for thing in my_list:
    print(thing, sep='\n')
