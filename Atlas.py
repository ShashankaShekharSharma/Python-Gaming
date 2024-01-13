import random
flag = 1
country_list=[
    'Canada', 'US', 'Mexico', 'Guatemala', 'Belize', 'El Salvador', 'Honduras', 'Costa Rica', 'Nicaragua', 'Panama',
    'Bermuda', 'Bahamas', 'Haiti', 'Cuba', 'Jamaica', 'Dominican Republic', 'Dominica', 'St. Kitts and Nevis',
    'St. Lucia', 'St. Vincent and The Grenadines', 'Barbados', 'Grenada', 'Trinidad and Tobago', 'Columbia', 'Venezuela',
    'Guyana', 'Suriname', 'Brazil', 'Ecuador', 'Peru', 'Bolivia', 'Paraguay', 'Chile', 'Argentina', 'Uruguay', 'Kosova',
    'Palestine', 'Western Sahara', 'Turkish Cyprus', 'Taiwan', 'Vatican City', 'Australia', 'New Zealand', 'Papua New Guinea',
    'Palau', 'Micronesia', 'Marshall Islands', 'Nauru', 'Vanuatu', 'Solomon Islands', 'Kiribati', 'Tuvalu', 'Tonga', 'Fiji',
    'Samoa', 'Yemen', 'Oman', 'UAE', 'Qatar', 'Bahrain', 'Saudi Arabia', 'Kuwait', 'Iraq', 'Jordan', 'Israel', 'Lebanon',
    'Syria', 'Cyprus', 'Turkey', 'Georgia', 'Armenia', 'Azerbaijan', 'Iran', 'Afghanistan', 'Pakistan', 'Turkmenistan',
    'Uzbekistan', 'Tajikistan', 'Kyrgyzstan', 'Kazakhstan', 'China', 'Mongolia', 'India', 'Nepal', 'Srilanka', 'Maldives',
    'Bhutan', 'Bangladesh', 'Myanmar', 'Thailand', 'Laos', 'Cambodia', 'Vietnam', 'Malaysia', 'Singapore', 'Brunei', 'Indonesia',
    'East Timor', 'Philippines', 'South Korea', 'North Korea', 'Japan', 'Morocco', 'Algeria', 'Tunisia', 'Libya', 'Egypt',
    'Mauritania', 'Mali', 'Senegal', 'Gambia', 'Guinea Bissau', 'Guinea', 'Sierra Leone', 'Liberia', 'Ivory Coast', 'Ghana',
    'Burkina', 'Togo', 'Benin', 'Niger', 'Nigeria', 'Chad', 'Cameroon', 'Central African Republic', 'North Sudan', 'South Sudan',
    'Eritrea', 'Djibouti', 'Ethiopia', 'Somalia', 'Equatorial Guinea', 'Gabon', 'Republic of Congo', 'Democratic Republic of Congo',
    'Uganda', 'Kenya', 'Rwanda', 'Burundi', 'Tanzania', 'Angola', 'Zambia', 'Malawi', 'Mozambique', 'Namibia', 'Botswana',
    'Zimbabwe', 'South Africa', 'Lesotho', 'Swaziland', 'Seychelles', 'Comoros', 'Madagascar', 'Mauritius', 'Cape Verde',
    'Sai Tome and Principe'
]

print(country_list)
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
  while user_input in country_list:
    countries_used.append(user_input)
    country_list.remove(user_input)
    computer = filter_countries_starting_with(user_input, country_list)
    print("Computer: " + computer)
  if user_input in countries_used:
    print("Game Over! You Lose")


#Expected output
#Player: Canada
#Computer: America
#Player: Australia
#Computer: Argentina
#Player: America
#Game Over! You Lose



