import chess

xd=chess.Board()

move=chess.Move(1,0)

print(xd.piece_map()[move.to_square])

print(xd.turn)

xd.push_san("e2e4")

print(xd.turn)