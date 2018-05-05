prices = ["24", "13", "16000", "1400"]
price_nums = [int(price) for price in prices]

print(prices)
print(price_nums)

dog = "poodle"
letters = [letter for letter in dog]
print(letters)

capital_letters = [letter.upper() for letter in letters]
print(capital_letters)

for letter in letters:
    capital_letters.append(letter.upper())

print(capital_letters)

no_oh_oh_no = [letter for letter in letters if letter != 'o']
print(no_oh_oh_no)

june_temperature = [72,65,59,87,69,50,40,73]
july_temperature = [24,61,73,72,57,25,34,44]
august_temperature = [100,60,58,83,82,42,55,64]
temperature = [june_temperature, july_temperature, august_temperature]
lowest_summer_temp = [min(temps) for temps in temperature]
print(lowest_summer_temp)

def multiple3(a):
    return a % 3 == 0

print(multiple3(4))
print(multiple3(6))