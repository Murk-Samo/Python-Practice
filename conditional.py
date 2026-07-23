conditional.

print("=====WELCOME=====")
print("choose one of them ")
print("1. want to be rich? ")
print("2. want to get married")
print("3. Rich + Family ")
while True:
  a = input("Enter a number 1, 2 or 3: ")
  if a in("1", "2", "3"):
    break
if a=="1":
  print("Nice! ")
elif a=="2":
  print("be successful before marriage. ")
elif a=="3":
  print("Good ")
