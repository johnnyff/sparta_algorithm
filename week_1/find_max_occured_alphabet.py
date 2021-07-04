input = "hello my name is johnny Kang"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    max_occured = alphabet_occurrence_array[0]
    max_index = 0
    for index in range(len(alphabet_occurrence_array)):
        if(alphabet_occurrence_array[index]>max_occured):
            max_oc = alphabet_occurrence_array[index]
            max_index = index
    answer = chr(ord("a")+max_index)


    return answer


result = find_max_occurred_alphabet(input)
print(result)