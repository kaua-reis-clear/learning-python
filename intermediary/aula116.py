# Creating files with Python + Context Manager with
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
with open(file_path, 'w') as file:
    print('Hello world')
    print('File will be closed')