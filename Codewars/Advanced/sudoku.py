def done_or_not(board):
    s = 0
    for i in board:
        for j in i:
           s += j
    if s == 405: # Won't work because every line will have 1-9, it's what's vertical that's to worry about.
        return "Finished!"
    print(s)
    return "Try Again!"


#WIP

"""
Write a function done_or_not passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.
"""
