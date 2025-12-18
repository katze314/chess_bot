import chess

xd=chess.Board()





#values of each piece in centipawn
piece_values=[0,100,300,350,500,900,100000]

#values for positions for each piece. 
#for white peaces, needs to be flipped for black pieces.
positional_values=[
    [],
    [
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 4, 4, 4, 4, 4, 4,
         8, 8, 8, 8, 8, 8, 8, 8,
        16,16,16,16,16,16,16,16,
        32,32,32,32,32,32,32,32
    ],
    [ 
         2, 3, 4, 4, 4, 4, 3, 2,
         3, 4, 6, 6, 6, 6, 4, 3,
         4, 6, 8, 8, 8, 8, 6, 4,
         4, 6, 8, 8, 8, 8, 6, 4,
         4, 6, 8, 8, 8, 8, 6, 4,
         4, 6, 8, 8, 8, 8, 6, 4,
         3, 4, 6, 6, 6, 6, 4, 3,
         2, 3, 4, 4, 4, 4, 3, 2
    ],
    [
         7, 7, 7, 7, 7, 7, 7, 7,
         7, 9, 9, 9, 9, 9, 9, 7,
         7, 9,11,11,11,11, 9, 7,
         7, 9,11,13,13,11, 9, 7,
         7, 9,11,13,13,11, 9, 7,
         7, 9,11,11,11,11, 9, 7,
         7, 9, 9, 9, 9, 9, 9, 7,
         7, 7, 7, 7, 7, 7, 7, 7
    ],
    [  
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         8, 8, 8, 8, 8, 8, 8, 8,
         8, 8, 8, 8, 8, 8, 8, 8
    ],
    [
         7, 7, 7, 7, 7, 7, 7, 7,
         7, 9, 9, 9, 9, 9, 9, 7,
         7, 9,11,11,11,11, 9, 7,
         7, 9,11,13,13,11, 9, 7,
         7, 9,11,13,13,11, 9, 7,
         7, 9,11,11,11,11, 9, 7,
        15,17,17,17,17,17,17,15,
        15,15,15,15,15,15,15,15  
    ],
    [
         8, 8, 8, 8, 8, 8, 8, 8,
         8, 8, 8, 8, 8, 8, 8, 8,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0
    ]
]
    

#computes the current board value, positive = white has better position
def board_value(board):    
    value=0
    #calculate values of figures on board
    for square in range(64):
        piece = board.piece_at(square)
        if(piece):
            if(piece.color):
                value+=piece_values[piece.piece_type]
                print(piece_values[piece.piece_type])
                value+=positional_values[piece.piece_type][square]
            else:
                value-=piece_values[piece.piece_type]
                value-=positional_values[piece.piece_type][chess.square_mirror(square)]
    return value
    



print(board_value(xd))


