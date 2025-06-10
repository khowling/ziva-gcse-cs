
# Create an array (list) of size 100, each element initialized to a single character (e.g., empty string)
numbers = [''] * 100


def display_count_of_free_numbers():
    count = 0
    for number in numbers:
        if number == '':
            count += 1
    print(f"There are {count} free numbers available.")
    

def set_player_number(player):
    index = int(input(f"Player {player}, enter a number between 0 and 99: "))
    if numbers[index] != '':
        print(f"Index {index} is already taken by player {numbers[index]}.")
        return
    numbers[index] = player
    print(f"Set index {index} to player {player}.")



while True:
    display_count_of_free_numbers()
    set_player_number('A')




