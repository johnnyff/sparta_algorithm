input = "abafecabade"


def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    not_repeated =[]
    for index in range(len(alphabet_occurrence_array)):
        if(alphabet_occurrence_array[index] ==1):
            not_repeated.append(chr(ord("a")+index))
    for char in string:
        if(char in not_repeated):
            return char


    return "_"


result = find_not_repeating_first_character(input)
print(result)