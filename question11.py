with open('class9.txt', 'r') as class9:
    try:
        class10A = open('class10A.txt', 'w')
        class10B = open('class10B.txt', 'w')
        class10C = open('class10C.txt', 'w')

        for i, line in enumerate(class9.readlines()):
            if i % 3 == 0:
                class10A.write(line)
            elif i % 3 == 1:
                class10B.write(line)
            elif i % 3 == 2:
                class10C.write(line)

    except Exception as err:
        print(f'**`{type(err).__name__} : {err}`**')
    finally:
        class10A.close()
        class10B.close()
        class10C.close()
