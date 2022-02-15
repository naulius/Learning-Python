# To create text and write in files:
# Example":
d = open("/home/natalia/example.text", "w")  # It has created a text file in Home.
d.write("hello")

# If you want to read the file:
# Example:
d = open("/home/natalia/example.text", "r")
content = d.read()
print(content)

# To close a file:
# Example:
content = d.close()
print(content)

with open("/home/natalia/example.text") as my_new_file:
    content = my_new_file.read()
    print(content)

# There are Reading, Writing and Appending modes to learn:
# mode = "r" is only to read.
# mode = "w" is only to write or overwrite new.
# mode = "a" is append only, it means it can add files.
# mode = " r+" is reading and writing.
# mode = " w+" is writing and reading. It also overwrites or create new files.

# We will create a new file in other way.
d = open("/home/natalia/my_new_example.text","w")
d.write("This is a new file")
d.close()
with open("/home/natalia/my_new_example.text", mode="r") as f:
    print(f.read())

# If you want to add a new text to the file:
# Example:
d = open("/home/natalia/my_new_example.text","w")
with open ("/home/natalia/my_new_example.text", mode="a") as f:
    f.write("for practising")

with open("/home/natalia/my_new_example.text", mode="r") as f:
    print(f.read())



