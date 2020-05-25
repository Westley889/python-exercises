import sys

def string_to_int(strings):
    final_value = 0
    num_list = []
    for chars in strings:
        num_list.append(ord(chars) - 48)
    for nums in range(0, len(num_list)):
        num_list[nums] *= 10 ** nums
        final_value += num_list[nums]
    return final_value

def int_to_string(numbers):
    fun = ""
    numbers = list(numbers)
    return fun.join(numbers)

word_num = sys.argv[1]

print(string_to_int(word_num))
print(int_to_string(word_num))