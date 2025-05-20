import random
chosen = ""
check_x = 5
check_y = 5
count_ai = 8
count_user = 8

print(63*"*")
print("*                   WELCOME TO BATTLESHIP                     *")
print(63*"-")
print("*  This is a game where you will attack your opponents ships  *")
print("*  Enter in a coordinate that you want to attack              *")
print("*  You will be told if you had a hit or not                   *")
print("*  You will be able to see what moves your opponent made      *")
print(63*"*")
print()

#Pick a board for the "AI"
matrix_ai = []

matrix_A_ai = [
    ["-", "X", "X", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["X", "-", "X", "X", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "X", "X", "X", "-"],
]

matrix_B_ai = [
    ["-", "-", "-", "-", "X"],
    ["-", "-", "X", "-", "X"],
    ["-", "-", "X", "-", "-"],
    ["X", "-", "-", "-", "-"],
    ["-", "-", "X", "X", "X"],
]

matrix_C_ai = [
    ["X", "-", "-", "-", "X"],
    ["-", "-", "-", "-", "X"],
    ["-", "-", "-", "-", "X"],
    ["X", "-", "-", "-", "-"],
    ["X", "-", "X", "X", "-"],
]
#choose a matrix for the ai
random_num = random.randint(0,3)
if random_num == 1:
    matrix_ai = matrix_A_ai
elif random_num == 2:
    matrix_ai = matrix_B_ai
else:
    matrix_ai = matrix_C_ai

#Make the empty matrix that the user can view later
check_board = [
    ["1", "-", "-", "-", "-", "-"],
    ["2", "-", "-", "-", "-", "-"],
    ["3", "-", "-", "-", "-", "-"],
    ["4", "-", "-", "-", "-", "-"],
    ["5", "-", "-", "-", "-", "-"],
    [" ", "1", "2", "3", "4", "5"]
]

#Make matrix options for User

print("Board option A:")
matrix_A_user = [
    ["X", "-", "-", "X", "-"],
    ["X", "-", "-", "X", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "X", "-", "-", "-"],
    ["-", "-", "X", "X", "X"],
]
for line in matrix_A_user:
    for item in line:
        print(item,end= " ")
    print()
print()
print("Board option B:")
matrix_B_user = [
    ["X", "-", "-", "-", "-"],
    ["-", "-", "X", "X", "-"],
    ["X", "-", "-", "-", "-"],
    ["X", "-", "X", "-", "-"],
    ["X", "-", "X", "-", "-"],
]
for line in matrix_B_user:
    for item in line:
        print(item,end= " ")
    print()
print()
print("Board option C:")
matrix_C_user = [
    ["-", "-", "-", "-", "X"],
    ["-", "-", "X", "-", "-"],
    ["-", "-", "X", "-", "-"],
    ["-", "-", "X", "-", "X"],
    ["X", "X", "-", "-", "X"],
]
for line in matrix_C_user:
    for item in line:
        print(item,end= " ")
    print()
print()

    
while chosen != "A" and chosen != "a" and chosen != "B" and chosen != "b" and chosen != "C" and chosen != "c":  
    chosen = input("Enter which board you would like to use (A, B, or C): ")
    
if chosen == "A" or chosen == "a":
    matrix_user = matrix_A_user
elif chosen == "B" or chosen == "b":
    matrix_user = matrix_B_user
else:
    matrix_user = matrix_C_user
print()

print("You selected this board!")
for line in matrix_user:
    for item in line:
        print(item,end= " ")
    print()
print()

print()
print("Here is a board for you to keep track of where you have attacked so far!")

for line in check_board:
    for item in line:
        print(item,end= " ")
    print()
print()

# actually running the game
while count_ai != 0 or count_user != 0:
    
    #Add while loop here so it keeps trying till its right
        
        
    while True:
        try:
            check_x = int(input("Enter the x coordinate you would like to attack: "))
            while check_x > 5:
                if check_x > 5:
                    print("Please enter a number less than or equal to 5")
                    check_x = int(input("Enter the x coordinate you would like to attack: "))
                    continue
                else: 
                    break
            break
        except ValueError:
            print("Please enter an integer.")
        
    #add while loop here so it keeps trying till it is right
    while True:
        try:
            check_y = int(input("Enter the y coordinate you would like to attack: "))
            while check_y > 5:
                if check_y > 5:
                    print("Please enter a number less than or equal to 5")
                    check_y = int(input("Enter the y coordinate you would like to attack: "))
                    continue
                else: 
                    break
            break
        except ValueError:
            print("Please enter an integer.")
            

    
    if matrix_ai[check_y-1][check_x-1] == "X" or matrix_ai[check_y-1][check_x-1] == "x":
        check_board[check_y-1][check_x] = "X"
        print()
        for line in check_board:
            for item in line:
                print(item,end= " ")
            print()
        count_user = count_user -1
        print("That was a HIT! You have " +str(count_user) +" ships left to hit.")
        print()
    else:
        check_board[check_y-1][check_x ] = "O"
        print()
        for line in check_board:
            for item in line:
                print(item,end= " ")
            print()
        print("That was a miss")
        print()
        

    print("*" *63)
    print()
    print("It is now your opponent's turn:")
    random_x = random.randint(1, 5)
    random_y = random.randint(1, 5)
    while True:
        if  matrix_user[random_y-1][random_x-1] == "/" or matrix_user[random_y-1][random_x-1] == "O":
            random_x = random.randint(1, 5)
            random_y = random.randint(1, 5)
        else:
            break
        
    if matrix_user[random_y-1][random_x-1] == "X" or matrix_user[random_y-1][random_x-1] == "x":
        count_ai = count_ai - 1
        print("Your opponent hit you, you have " +str(count_ai) +" ships left!")
        matrix_user[random_y-1][random_x-1] = "/"
        print()
        print("Your board's status (O = miss, / = hit):")
        for line in matrix_user:
            for item in line:
                print(item,end= " ")
            print()
        if count_ai == 0:
            break
        print()
    else:
        print("You opponent missed your ships.")
        matrix_user[random_y-1][random_x-1] = "O"
        print()
        print("Your board's status (O = miss, / = hit):")
        for line in matrix_user:
            for item in line:
                print(item,end= " ")
            print()
        print()
    print("*" *63)
    
    
    
    print()
    print("Chose a location to attack:")
    for line in check_board:
        for item in line:
            print(item,end= " ")
        print()
    if count_user == 0:
        break
    print("You have " +str(count_user) +" ships left to hit.")
    print()
    
#winning / losing screen
print()
if count_user == 0:
    print("Game Over!")
    print("You win! :)")
else:
    print("Game Over!")
    print("You lost :(")


