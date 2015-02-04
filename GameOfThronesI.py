__author__ = 'bogdan.cornianu'

text = raw_input()

palindrome = 'NO'
already_searched = []

if len(text) % 2 == 0:
    for char in text:
        if char not in already_searched and text.count(char) % 2 == 0:
            palindrome = 'YES'
            already_searched.append(char)
        elif char not in already_searched and text.count(char) % 2 != 0:
            palindrome = 'NO'
            already_searched.append(char)
else:
    except_one_char = 0
    rest_of_chars = 0
    for char in text:
        if char not in already_searched and text.count(char) % 2 == 0:
            already_searched.append(char)
            rest_of_chars = 1
        elif char not in already_searched and text.count(char) % 2 != 0\
                and except_one_char == 0:
            except_one_char += 1
            already_searched.append(char)
        elif char not in already_searched and text.count(char) % 2 != 0\
                and except_one_char == 0:
            already_searched.append(char)
            rest_of_chars = 0
    if rest_of_chars == 1 and except_one_char > 0:
        palindrome = 'YES'
    else:
        palindrome = 'NO'

print palindrome