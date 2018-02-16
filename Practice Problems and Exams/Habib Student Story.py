continueIt = True
while continueIt == True:
	print("This is a story of an incredible Habib University Student")
	name = input("His name was... ")
	age = int(input("And his age was... "))

	print(name, "got up in the morning and decided to... ")
	print("Enter 1 to shower")
	print("Enter 2 to not shower")
	shower = int(input())

	print("Then ", name, "decided to... ")
	print("Enter 1 to eat breakfast")
	print("Enter 2 to not eat breakfast")
	breakfast = int(input())

	print(name, "had to go to Habib University on his bike. ")
	if shower == 2:
		print("Since he had not taken a shower, he was feeling sleepy. ")
	if breakfast == 2:
		print("Having no breakfast made him drowsy. ")
		
	if shower == 2 and breakfast == 2:
		print("With the combination of these two elements, he went headon into on coming traffic and had a tragic accident.")
		print(name, "Died at the ripe age of ", age)
	elif shower == 1 and breakfast == 1:
		print("He reached Habib University fresh and safe.")
	else:
		print("He reached Habib University but not in the best of moods")
	print("Do you want to play another story? Press y or n")
	ans = input()
	if ans == "n":
		continueIt = False