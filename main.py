import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row['letter']: row['code'] for (index, row) in nato_data.iterrows()}

while True:
    user_input = input("Enter a word: ").upper()
    try:
        answer = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(answer)
        break
