import cv2
# from tqdm import tqdm

# my idea here is to load predefined image of sudoku board and draw into it.
def save_board(board, name):
    # loads empty sudoku board into img
    img = cv2.imread("sudokuboard.png")
    # gap equals space between each number
    gap = 102
    actual_line = -18
    # for line in tqdm(board):
    for line in board:
        print(line)
        if "-" in str(line):
            pass
        else:
            actual_char = 25
            actual_line += gap
            for char in line:
                if char == "|":
                    continue
                cv2.putText(img, str(char), (actual_char, actual_line), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,0))
                actual_char += gap
    cv2.imwrite("{}.png".format(str(name)), img)


# brd =  [[7, ' ', ' ', '|', ' ', ' ', ' ', '|', 4, 3, ' '], 
#         [4, 3, ' ', '|', ' ', 2, ' ', '|', 6, ' ', ' '], 
#         [9, 1, 6, '|', ' ', ' ', ' ', '|', 8, ' ', 2], 
#         ['- - - - - - - - - - -'], 
#         [' ', 8, 7, '|', ' ', ' ', ' ', '|', 3, ' ', ' '], 
#         [' ', ' ', ' ', '|', ' ', 8, ' ', '|', 9, ' ', ' '], 
#         [1, ' ', 9, '|', ' ', 4, 3, '|', ' ', ' ', ' '], 
#         ['- - - - - - - - - - -'], 
#         [6, ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', 8, 7], 
#         [8, ' ', 2, '|', ' ', 1, 6, '|', ' ', 4, 3], 
#         [' ', 4, ' ', '|', ' ', ' ', ' ', '|', ' ', 6, ' ']]
# save_board(brd)

