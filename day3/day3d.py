# section 1

user_input = input("Enter a word please: ")  
char_index_dict = {}

for letter_position, letter in enumerate(
    user_input
):  
    print(f"At position {letter_position}, we have the letter {letter}")
    if (
        letter in char_index_dict.keys()
    ):  
        char_index_dict[letter].append(
            letter_position
        )  
    else:  
        char_index_dict[letter] = [
            letter_position
        ]  

print(char_index_dict)

word_len = 0
for key, position_list in char_index_dict.items():
    for position in position_list:
        if position > word_len:
            word_len = position
word_len += 1
print(f"The word has length {word_len}")

rebuild_index = 0
rebuilt_word = ""
for rebuild_index in range(0, word_len):
    found_letter = False
    for key, position_list in char_index_dict.items():
        for position in position_list:
            if position == rebuild_index:
                rebuilt_word += key
                rebuild_index += 1
                found_letter = True
                break
        if found_letter:
            break

print(f"The rebuilt word is : {rebuilt_word}")

#section 2

Product_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20",
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200",
}

wallet_P = input("how much you have: ")
wallet_P = int(wallet_P.replace("$", "").replace(",", ""))

Good_items = []
for item, cost_str in Product_purchase.items():
    cost_int = int(cost_str.replace("$", "").replace(",", ""))
    if wallet_P >= cost_int:
        print(f"You can buy {item}")
        Good_items.append(item)

if len(Good_items) > 0:
    Good_items.sort()
    print(f"payment has been sucessful {Good_items}")
else:
    print("it not enoght ;_;")

















