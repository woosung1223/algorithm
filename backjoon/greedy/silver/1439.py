# min(0을 뒤집었을 때, 1을 뒤집었을 때)
# 압축 후 -> 0, 1 개수를 세면 됨

string = input()
compressed_string = ""

before_char = string[0]
for character in string:
    if before_char != character:
        compressed_string += before_char
        before_char = character

compressed_string += before_char
print(min(compressed_string.count('0'), compressed_string.count('1')))