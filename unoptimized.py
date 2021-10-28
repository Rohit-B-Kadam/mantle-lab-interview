class Frequency:
    def __init__(self, input=None):
        self.input = input


alpha_pos = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

count_array = [0] * 26

input_sample = ['welcome', 'To', 'the', 'crib', 'And', 'have', 'a', 'Cookie']

sample = ''


# for i in input_sample:
#     sample = sample + i

sample = ''.join(input_sample)
print(sample)

sample = sample.lower()
print(sample)

print(ord('a'))

for ch in sample:
    array_position = -1
    ord('a')
    # for j in range(len(alpha_pos)):
    #     if alpha_pos[j] == ch:
    #         array_position = j
    if array_position != -1:
        count_array[array_position] += 1


# for i in range(len(sample)):
#     store_char = sample[i]
#     if sample[i].isupper():
#         store_char = sample[i].lower()
#     array_position = -1
#     for j in range(len(alpha_pos)):
#         if alpha_pos[j] == store_char:
#             array_position = j
#     for j in range(len(count_array)):
#         if j == array_position:
#             count_array[j] += 1

# for i in range(len(alpha_pos)):
#     if count_array[i] != 0:
#         print(alpha_pos[i] + " = " + str(count_array[i]))