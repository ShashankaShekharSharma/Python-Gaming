
import random

class AtlasGame:

    def __init__(self):
        country_list = ['Canada', 'USA', 'Mexico', 'Guatemala', 'Belize', 'El Salvador', 'Honduras', 'Costa Rica', 'Nicaragua', 'Panama',
      'Bermuda', 'Bahamas', 'Haiti', 'Cuba', 'Jamaica', 'Dominican Republic', 'Dominica', 'St. Kitts and Nevis',
      'St. Lucia', 'St. Vincent and The Grenadines', 'Barbados', 'Grenada', 'Trinidad and Tobago', 'Columbia', 'Venezuela',
      'Guyana', 'Suriname', 'Brazil', 'Ecuador', 'Peru', 'Bolivia', 'Paraguay', 'Chile', 'Argentina', 'Uruguay', 'Kosova',
      'Palestine', 'Western Sahara', 'Turkish Cyprus', 'Taiwan', 'Vatican City', 'Australia', 'New Zealand', 'Papua New Guinea',
      'Palau', 'Micronesia', 'Marshall Islands', 'Nauru', 'Vanuatu', 'Solomon Islands', 'Kiribati', 'Tuvalu', 'Tonga', 'Fiji',
      'Samoa', 'Yemen', 'Oman', 'UAE', 'Qatar', 'Bahrain', 'Saudi Arabia', 'Kuwait', 'Iraq', 'Jordan', 'Israel', 'Lebanon',
      'Syria', 'Cyprus', 'Turkey', 'Georgia', 'Armenia', 'Azerbaijan', 'Iran', 'Afghanistan', 'Pakistan', 'Turkmenistan',
      'Uzbekistan', 'Tajikistan', 'Kyrgyzstan', 'Kazakhstan', 'China', 'Mongolia', 'India', 'Nepal', 'Srilanka', 'Maldives',
      'Bhutan', 'Bangladesh', 'Myanmar', 'Thailand', 'Laos', 'Cambodia', 'Vietnam', 'Malaysia', 'Singapore', 'Brunei', 'Indonesia', 'East Timor', 'Philippines', 'South Korea', 'North Korea', 'Japan', 'Morocco', 'Algeria', 'Tunisia', 'Libya', 'Egypt', 'Mauritania', 'Mali', 'Senegal', 'Gambia', 'Guinea Bissau', 'Guinea', 'Sierra Leone', 'Liberia', 'Ivory Coast', 'Ghana', 'Burkina', 'Togo', 'Benin', 'Niger', 'Nigeria', 'Chad', 'Cameroon', 'Central African Republic', 'North Sudan', 'South Sudan', 'Eritrea', 'Djibouti', 'Ethiopia', 'Somalia', 'Equatorial Guinea', 'Gabon', 'Republic of Congo', 'Democratic Republic of Congo', 'Uganda', 'Kenya', 'Rwanda', 'Burundi', 'Tanzania', 'Angola', 'Zambia', 'Malawi', 'Mozambique', 'Namibia', 'Botswana', 'Zimbabwe', 'South Africa', 'Lesotho', 'Swaziland', 'Seychelles', 'Comoros', 'Madagascar', 'Mauritius', 'Cape Verde', 'Sai Tome and Principe'] 
        self.country_list = sorted(country_list)
        self.used_countries = []

    def is_valid_country(self, country):
        return country.lower() in [c.lower() for c in self.country_list]

    def checkCountry(self, target):
        # Check if the target country is valid and follows the rule
        return (
            self.is_valid_country(target) and
            (not self.used_countries or
             (target.lower() not in [country.lower() for country in self.used_countries] and
              target.lower().startswith(self.used_countries[-1][-1].lower())))
        )

    def computerChoice(self):
        # Find valid choices using binary search
        last_letter = self.used_countries[-1][-1].lower() if self.used_countries else None
        valid_choices = [country for country in self.country_list if last_letter and country.lower().startswith(last_letter) and country not in self.used_countries]

        if not valid_choices:
            return None, True  # No valid choices, defeat

        return random.choice(valid_choices), False

    def main(self):
        print("Welcome to the Atlas Game!")
        print("Let's begin...\n")

        while True:
            # User's turn
            user_input = input("Your turn! Enter a country name: ")
            if self.checkCountry(user_input):
                print(f"{user_input} is a valid choice!\n")
                self.used_countries.append(user_input)
            else:
                print(f"Invalid choice or country not in the list. You lose!\n")
                break

            # Computer's turn
            computer_choice, is_defeat = self.computerChoice()
            if not is_defeat:
                print(f"Computer chooses: {computer_choice}\n")
                self.used_countries.append(computer_choice)
            else:
                print("Computer cannot make a valid choice. You win!\n")
                break


# Instantiate the AtlasGame class
game = AtlasGame()

# Call the main method to start the game
game.main()
