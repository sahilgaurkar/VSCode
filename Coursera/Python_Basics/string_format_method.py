scores = [("Rodney Dangerfield", -1), ("Sahil", 100), ("You", 50)]


for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}".format(name,score))





origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}'.format(origPrice, discount, newPrice)
print(calculation)