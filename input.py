

# # Taking basic user input
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# # Taking 6 subjects and their marks
# subjects = []
# marks = []
# for i in range(6):
#     sub = input(f"Enter name of subject {i+1}: ")
#     mark = input(f"Enter marks for {sub}: ")
#     subjects.append(sub)
#     marks.append(mark)

# # Taking percentage input
# percentage = input("Enter your overall percentage: ")

# # Printing the details
# print("\n--- Student Details ---")
# print("Name        :", name)
# print("Age         :", age)
# print("\nSubjects and Marks:")
# for i in range(6):
#     print(f"{subjects[i]} : {marks[i]}")






name = input('Enter Student name :-')
age = input('Enter Student Age :-')
#sub = input ('Enter sub name:-')

Hindi=int(input('Enter your Hindi marks:-'))
English=int(input('Enter your English marks:-'))
Math=int(input('Enter your Math marks:-'))
Biology=int(input('Enter your Biology marks:-'))
History=int(input('Enter your History marks:-'))




print("Your name is - " + name)
print("your age is- "+ age)

Total = Hindi + English + Math + Biology + History

per = (Total / 500) * 100

print("your total marks is :=" + str(Total))
print(per)

