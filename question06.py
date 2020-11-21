def copy_string(string1, string2=''):
    if string1 == '':
        return string2
    else:
        return string2 + string1[0] + copy_string(string1[1:])


str1 = input("Enter a string: ")
str2 = 'good'
print(f"Output: {copy_string(str1, str2)}")
