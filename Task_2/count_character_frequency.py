sample_String = "ppython"
char_count = {}
for char in sample_String:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)