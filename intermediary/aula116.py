import os
# with open (context manager) and TextIOWrapper useful methods
# We use open function to open
# a file in Python (it may or may not exist)
# Behaviors:
# r (read), w (write), x (create)
# a (writes at the end), b (binary)
# t (text mode), + (read and write)
# Context manager - with (open and close)
# Useful methods
# write, read
# writelines (write multiple lines)
# seek (moves the cursor)
# readline (read line)
# readlines (read lines)
# os.remove or unlink - deletes the file
# os.rename - rename or move the file
# json.dump = generates a json file
# json.load
file_path = 'aula116.txt'

# file = open(file_path, 'w')
# #
# file.close()

# with open(file_path, 'w+') as file:
#     file.write('Line 1\n')
#     file.write('Line 2\n')
#     file.writelines(
#         ('Line 3\n', 'Line 4\n')
#     )
#     file.seek(0, 0)
#     print(file.read())
#     print('Reading')
#     file.seek(0, 0)
#     print(file.readline(), end='')
#     print(file.readline().strip())
#     print(file.readline().strip())

#     print('READLINES')
#     file.seek(0, 0)
#     for line in file.readlines():
#         print(line.strip())


# print('#' * 10)

# with open(file_path, 'r') as file:
#     print(file.read())

with open(file_path, 'w', encoding='utf8') as file:
    file.write('Attention\n')
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.writelines(
        ('Line 3\n', 'Line 4\n')
    )

# os.remove(file_path) # ou unlink
# os.rename(file_path, 'aula116-2.txt')