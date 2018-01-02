# make a list to hold onto our items
shopping_list = []

def show(items):
    for item in items:
        print(item)

# print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break

    # be able to see what's currently on the list
    elif new_item == 'SHOW':
        show(shopping_list)

    # add new items to our list
    shopping_list.append(new_item)

# print out the list
print("Here's your list:")

show(shopping_list)
