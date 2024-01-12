import random
line1 = ["A1", "B1", "C1"]
line2 = ["A2", "B2", "C2"]
line3 = ["A3", "B3", "C3"]
MAP = [line1, line2, line3]
print(f"{line1}\n{line2}\n{line3}")
print("Hiding your treasure! X marks the spot.")

# AI---------------------------------AI
AI_CHOICE = [
    "A1", "B1", "C1",
    "A2", "B2", "C2",
    "A3", "B3", "C3"]
AI_POSITION = random.choice(AI_CHOICE)
print(AI_POSITION)
# AI---------------------------------AI
game_is_on = True

while game_is_on:

    position = input("POSITION > ").title()

    # Where do you want to put the treasure?
    # Your code below
    letter = position[0].lower()

    abc = ["a", "b", "c"]
    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1
    MAP[number_index][letter_index] = "X"

    if position == AI_POSITION:
        MAP[number_index][letter_index] = "💎"
        print(f"{line1}\n{line2}\n{line3}")
        print("Correct!, SUUUUUUUUI🥳 congratulations! treasure <<wow")
        game_is_on = False

    else:
        print("tray again")
        print(f"{line1}\n{line2}\n{line3}")

    if position != AI_POSITION:
        answer_1 = input("continue? "
                         "(sorry, just write : 'no'"
                         ", for ending the game (: ) here: ").title()
        if answer_1 == "No":
            game_is_on = False
        else:
            pass
    else:
        pass
