file = open('data.txt', 'w')
file.write("The first line. ")
file.write("The second line\n")
file.write("\tThe third line")
file.close()


file = open('data.txt', 'r')
text=file.read()
print(text)
file.close()

file = open('data.txt', 'a')
file.write("\n\nThe fourth line. ")
file.write("\n\tThe fifth line\n")
file.write("\tThe sixth line")
for i in range(10):
    file.write(" " + str(i))
file.close()

file = open('data.txt', 'r')
text=file.read()
print(text)
file.close()


for letter in text:
    print(letter, end=" ")

