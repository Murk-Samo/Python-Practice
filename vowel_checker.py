vowel_checker.
while True:
  ask = input("Do you want to check if letter is vowel or consonant? ").lower()
  if ask == "no":
    break
  elif ask != "yes":
    print("Enter only yes or no: ")
    continue
  print("====VOWEL CHECKER====")
  letter = input("Enter a letter: ").lower()
  if len(letter) !=1 or not  letter.isalpha():
    print("INVALID INPUT")
  elif letter in ("aeiou"):
    print(f"{letter} is a vowel. ")
  else:
    print(f"{letter} is consonant")
  again = input("Do you want to check again? ").lower()
  if again in ("yes"):
    continue
  elif again in ("no"):
    break
  else:
    notvalid = input("Enter only yes or no: ")
    if notvalid in ("yes"):
      continue
    elif notvalid in ("no"):
      print("THANKS.")
      break
    else:
      print("Program crashed.")
