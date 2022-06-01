#Made by Alex
#Special thanks to the answer by Alain T in this post https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python

#======Libraries======
import random
import copy

#======Functions======
#Text on startup
def introduction():
    print("Sudoku!\n")

    print('''Rules:
    1) Each mini-board has to contain the symbols 1-9.
    2) Each symbol can only appear once in a row, column, or mini-board.
    3) For every "0" symbol, replace that cell with what you think the correct symbol is.
    4) After filling everything in, check your answer with the full board.''')

#Formula to validate sudoku pattern
def validate(x, y):
    offsets = (3 * (x % 3) + x // 3 + y) % 9 # Calculates the offsets so the numbers fit on a valid 9x9 Sudoku puzzle
    return offsets

#======Main======
def main():
    #Variables
    board = [] # Main board
    rows = [] # Horizontal
    cols = [] # Vertical
    cells = random.sample(range(1, 10), 9) # Unique range of elements to create cells in each row

    #Enter Input Loop
    while True:
        #Difficulty Input
        try:
            difficulty = float(input("Enter a difficulty (1-99): "))

            #Bad inputs
            if difficulty < 0:
                raise Exception("Difficulty cannot be negative!")
            elif difficulty == 0:
                raise Exception("Difficulty cannot be 0!")
            elif difficulty > 99:
                raise Exception("Difficulty cannot be more than 99!")
            elif difficulty.is_integer() == False:
                raise Exception("Difficulty cannot be floating point values.")
        #Error handling (general)
        except ValueError:
            print("Difficulty must be an integer value.\n")
        #Error handling (specific)
        except Exception as specificError:
            print(specificError, end = "\n\n")
        #Exit Input Loop
        else:
            difficulty = int(difficulty)
            print()
            break

    #Parent Row
    for row in random.sample(range(3), 3): # Loops through a random range of 3 numbers
        for r in random.sample(range(3), 3): # Loops through another random range of 3 numbers, effectively multiplying by 3 and creating a whole row with 9 shuffled elements
            rows.append(r * 3 + row)
    
    #Parent Column
    for col in random.sample(range(3), 3): # Columns use the same method as the rows
        for c in random.sample(range(3), 3): # 9 elements in a column, all randomized
            cols.append(c * 3 + col)

    #Main Board
    for r in rows: # Building the main board
        rank = [] # Local variable to append each row later
        for c in cols: # Creating a plane
            rank.append(cells[validate(r, c)]) # Validate random cells in rank
        board.append(rank) # Append rank to the main board

    hidden_board = copy.deepcopy(board) # Deep copies list and creates the hidden board

    #Difficulty
    for rank in hidden_board:
        for cell in range(len(rank)): # Goes through each cell
            if random.randint(1, 100) <= difficulty: # Random chance for difficulty
                rank[cell] = 0 # "0" is a placeholder for nothing

    #Obstructed Board
    for rank in hidden_board:
        print(*rank) # Prints each line

    print("\nPress enter to see the full board.")

    input()

    #Full Board
    for rank in board:
        print(*rank) # Prints each line

#======Execution Check======
if __name__ == '__main__':
    introduction()

    play = True

    while(play):
        print() # Spacer
        main()
        print() # Spacer

        #Enter Input Loop
        while True:
            response = input("Would you like to play again (y/n): ").lower()

            if response == "y":
                play = True
            elif response == "n":
                play = False
            #Error
            else:
                print("Input error.\n")
                continue
            break # Exit input loop