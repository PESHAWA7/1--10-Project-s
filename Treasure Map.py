game_is_on = True
while game_is_on:
    line1 = ["⬜️", "️⬜️", "️⬜️"]
    line2 = ["⬜️", "⬜️", "️⬜️"]
    line3 = ["⬜️️", "⬜️️", "⬜️️"]
    MAP = [line1, line2, line3]
    print("Hiding your treasure! X marks the spot.")
    position = input("enter the position please ")

    # Where do you want to put the treasure?

    letter = position[0].lower()
    abc = ["a", "b", "c"]
    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1
    MAP[number_index][letter_index] = "X"

    print(f"{line1}\n{line2}\n{line3}")

    if input("do yu wanna to play again? "
             "(sorry just no for ending the game (: ) here: ").title() == "No":
        game_is_on = False
    else:
        pass
