print("Welcome to Tic Tac Toe ")
print(f"""---------------------
| (1 1) (1 2) (1 3) |
| (2 1) (2 2) (2 3) |
| (3 1) (3 2) (3 3) |
---------------------""")
s = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
possible = ["1", "2", "3"]
choix = "X"
attempt = 1
print("Player X start the game ")
while True:
    if attempt % 2 == 0:
        choix = "O"
        print("player O turn ")
    else:
        choix = "X"
        print("player X turn ")
    attempt+=1
    while True:
        cordinate = input(" enter the cordinate : ").split()
        while (cordinate[0] not in possible) or (cordinate[1] not in possible):
            print("You should enter numbers!")
            cordinate = input().split()
        try:
            abscisse = int(cordinate[0])
            ordonne = int(cordinate[1])
            if abscisse > 3 or ordonne > 3 or abscisse < 1 or ordonne < 1:
                print("Coordinates should be from 1 to 3!")
                cordinate = input().split()
                abscisse = int(cordinate[0])
                ordonne = int(cordinate[1])
            k = abs(abscisse - ordonne)
            if abscisse == 1:
                if (abscisse - ordonne) == -k and (ordonne - abscisse) == k:
                    if s[k] == "_":
                        s[k] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    if s[k + 2] == "_":
                        s[k + 2] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
            elif abscisse == 2:
                if k == 0:
                    if s[4] == "_":
                        s[4] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                elif (abscisse - ordonne) == k and (ordonne - abscisse) == -k:
                    if s[k + 2] == "_":
                        s[k + 2] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    if s[k + 4] == "_":
                        s[k + 4] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
            else:
                if k == 0:
                    if s[8] == "_":
                        s[8] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                elif (abscisse - ordonne) == 2:
                    if s[6] == "_":
                        s[6] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    if s[7] == "_":
                        s[7] = choix
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
        except ValueError:
            print("You should enter numbers!")
    print(f"""---------
| {s[0]} {s[1]} {s[2]} |
| {s[3]} {s[4]} {s[5]} |
| {s[6]} {s[7]} {s[8]} |
---------""")
    ls = [s[0] + s[1] + s[2],
          s[3] + s[4] + s[5],
          s[6] + s[7] + s[8],
          s[0] + s[3] + s[6],
          s[1] + s[4] + s[7],
          s[2] + s[5] + s[8],
          s[0] + s[4] + s[8],
          s[6] + s[4] + s[2]]
    if "XXX" in ls:
        print("X wins")
        break
    elif "OOO" in ls:
        print("O wins")
        break