def insert_itemnode(array):
    member_details = tuple()
    member_details += (int(input("Enter member no:")), )
    member_details += (input("Enter name of member:"), )
    member_details += (int(input("Enter age of member:")), )
    array.append(member_details)


def delete_itemnode(array):
    if len(array) > 0:
        array.pop(0)


queue = []
for i in range(2):
    insert_itemnode(queue)
delete_itemnode(queue)
print(queue)
