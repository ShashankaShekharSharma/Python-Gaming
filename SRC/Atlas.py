import tkinter as tk
from tkinter import simpledialog
import random

class AtlasGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Atlas Game")

        self.used_countries_label = tk.Label(self.root, text="Used Countries:")
        self.used_countries_label.pack()

        self.computer_choice_label = tk.Label(self.root, text="")
        self.computer_choice_label.pack()

        self.game = AtlasGame()

        self.play_atlas_game()

    def play_atlas_game(self):
        while True:
            user_choice = self.get_user_choice()
            if user_choice is None:  # User clicked Cancel or closed the input dialog
                break

            result = self.game.check_and_append(user_choice)
            self.update_labels(self.game.used_countries, self.used_countries_label, "Used Countries:")

            if result["valid"]:
                self.update_labels([f"Computer Choice: {result['computer_choice']}"], self.computer_choice_label, "")
            else:
                self.display_result(result["message"])
                break

    def get_user_choice(self):
        user_choice = simpledialog.askstring("Atlas Game", "Enter a country name:")
        return user_choice

    def update_labels(self, data, label, label_text):
        formatted_data = "\n".join(data)
        label_text += f"\n{formatted_data}"
        label.config(text=label_text)

    def display_result(self, result):
        self.used_countries_label.config(text=f"{result}")
        if "Computer Choice" in result:
            self.computer_choice_label.config(text=result["Computer Choice"])
        self.root.mainloop()

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
        return (
            self.is_valid_country(target) and
            (not self.used_countries or
             (target.lower() not in [country.lower() for country in self.used_countries] and
              target.lower().startswith(self.used_countries[-1][-1].lower())))
        )

    def computerChoice(self):
        last_letter = self.used_countries[-1][-1].lower() if self.used_countries else None
        valid_choices = [country for country in self.country_list if last_letter and country.lower().startswith(last_letter) and country not in self.used_countries]

        if not valid_choices:
            return None, True  # No valid choices, defeat

        return random.choice(valid_choices), False

    def check_and_append(self, country):
        if self.checkCountry(country):
            self.used_countries.append(country)
            computer_choice, is_defeat = self.computerChoice()
            return {"valid": True, "computer_choice": computer_choice}
        else:
            return {"valid": False, "message": f"Invalid choice or country not in the list. You lose!"}

if __name__ == "__main__":
    atlas_game_gui = AtlasGameGUI()
