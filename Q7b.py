def draw_dash():
    print("--- "*board_size)

def draw_pipe():
    print("|   "*board_size)

board_size = int(input("Enter the size of the board:"))

for i in range (0,board_size):
                       draw_dash()
                       draw_pipe()
draw_dash()
