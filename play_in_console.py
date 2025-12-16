import chess

board = chess.Board()

print("Welcome to Chess")
print("White plays the Uppercase Letters")
print("Black moves the lowercase Letters")


print(board)

white=True
while(not board.is_game_over()):
    print(["Black to move, please enter a move", "White to move, please enter a move"][white], end=" ")
    c=input()
    while (not chess.Move.from_uci(c) in board.legal_moves):
        print("This is not a legal move")
        print("please enter a legal move:")
        c=input()
    board.push_san(c)
    print(board)
print("result: "+board.result())


