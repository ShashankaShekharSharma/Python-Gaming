import random
flag = 1
a = ['australia', 'argentina', 'america']
b = ['brazil', 'bangladesh']
c = ['canada']
countries = a+b+c
print(countries)
countries_used = []
def filter_countries_starting_with(letter, countries):
    filtered_countries = [country for country in countries if country.lower().startswith(letter.lower())]
    if filtered_countries !=[]:
      computer=random.choice(filtered_countries)
      countries.remove(computer)
      countries_used.append(computer)
    else:
      print("You Win")
      flag = -1
while flag == 1:
  user_input = input("Player: ").lower()
  while user_input in countries:
    countries_used.append(user_input)
    countries.remove(user_input)
    computer = filter_countries_starting_with(user_input, countries)
    print("Computer: " + computer.capitalize())
  if user_input in countries_used:
    print("Game Over! You Lose")


#Expected output
#Player: Canada
#Computer: America
#Player: Australia
#Computer: Argentina
#Player: America
#Game Over! You Lose



