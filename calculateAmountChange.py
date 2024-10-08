amount = eval(input("Enter an amount, for example, 11.56:"))
remainingAmount = int(amount * 100)

numberOfOneDollar = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarter = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDines = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", amount, "consist of\n", 
      "\t", numberOfOneDollar, "dollars\n",
      "\t", numberOfQuarter, "dollars\n",
      "\t", numberOfDines, "dollars\n",
      "\t", numberOfNickels, "dollars\n",
      "\t", numberOfPennies, "dollars\n"
      

)