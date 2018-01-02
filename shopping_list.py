# make a list to hold onto our items
shopping_list = []

# show what's currently on the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

# print out instructions on how to use the app
def show_help():
    print("Enter 'DONE' to stop adding items.")
    print("Enter 'SHOW' to see what's currently on the list.")
    print("Enter 'HELP' for this help.")

# add new items to our list
def add_item(new_item):
    shopping_list.append(new_item)
    message = "Added {} to the list. List now has {} items."
    print(message.format(new_item, len(shopping_list)))

print("What should we pick up at the store?")

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        show_list()
        continue
    elif new_item == 'HELP':
        show_help()
        continue
    add_item(new_item)

# print out the list

show_list()
