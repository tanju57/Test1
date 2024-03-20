x = 5
print(x>3 and x<10)

y = 12
print(y>10 and y%5 == 0)

x = 5
print(x<3 or x>10)

y = 12
print(y<10 or y%2 ==0)

x = 5
print(not(x>3 and x<10))

y = 12
print(not(y>10 and y%5 == 0))

user_age = int(input("Enter your age: "))
is_student = input("Are you a student? {yes/no}: ").lower()
eligible_for_discount = (user_age <= 12) or (13 <= user_age <= 19 and is_student == 'Yes')
if eligible_for_discount:
    print("Congrats! You are eligible for a discount.")
else:
    print("Sorry, you are not eligible for a discount.")
