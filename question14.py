import pickle
print("1.adding a new product")
print("2.search a product using id")
print("3.display product whose price less than 10")
print("4.delete product whose quantity is less than 10")
print("5.decrease the price of products by 3 whose quantity is lessthan 10")

choice = int(input("enter your numbered choice: "))

if choice == 1:
    f = open("product.pdf", "wb")
    prod_id = input("enter product id here: ")
    name = input("enter product name here: ")
    price = int(input("enter product price here: "))
    quantity = int(input("enter quantity product here: "))
    record = (prod_id, name, price, quantity)
    pickle.dump(record, f)

elif choice == 2:
    f = open("product.pdf", "rb")
    user = input("enter product id here: ")
    try:
        while True:
            r = pickle.load(f)
            if user == r[0]:
                print(r)

    except EOFError:
        f.close()

elif choice == 3:
    f = open("product.pdf", "rb")
    try:
        while True:
            r = pickle.load(f)
            if r[2] <= 10:
                print(r)

    except EOFError:
        f.close()

elif choice == 4:
    f = open("product.pdf", "rb")
    try:
        while True:
            r = pickle.load(f)
            if r[3] <= 10:
                del r
    except EOFError:
        f.close()

else:
    f = open("product.pdf", "rb")
    try:
        while True:
            r = pickle.load(f)
            if r[3] <= 10:
                r[2] -= 3
    except EOFError:
        f.close()
