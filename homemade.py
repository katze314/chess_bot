"""
Some example classes for people who want to create a homemade bot.

With these classes, bot makers will not have to implement the UCI or XBoard interfaces themselves.
"""
import chess
from chess.engine import PlayResult, Limit
import random
from lib.engine_wrapper import MinimalEngine
from lib.lichess_types import MOVE, HOMEMADE_ARGS_TYPE
import logging
import math


# Use this logger variable to print messages to the console or log files.
# logger.info("message") will always print "message" to the console or log file.
# logger.debug("message") will only print "message" if verbose logging is enabled.
logger = logging.getLogger(__name__)


class ExampleEngine(MinimalEngine):
    """An example engine that all homemade engines inherit."""


# Bot names and ideas from tom7's excellent eloWorld video

#values of each piece in centipawn
#piece_values={chess.Piece.from_symbol('K'):100000, chess.Piece.from_symbol('R'): 500,chess.Piece.from_symbol('Q'): 900,chess.Piece.from_symbol('B'): 350, chess.Piece.from_symbol('N'): 300, chess.Piece.from_symbol('P'):100,chess.Piece.from_symbol('k'):100000, chess.Piece.from_symbol('r'): 500,chess.Piece.from_symbol('q'): 900,chess.Piece.from_symbol('b'): 350, chess.Piece.from_symbol('n'): 300, chess.Piece.from_symbol('p'):100, 'K':100000, 'R': 500, 'Q': 900,'B': 350, 'N': 300, 'P':100,'k':100000, 'r': 500,'q': 900,'b': 350, 'n': 300, 'p':100, None: 0}

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
    
#white is maximizing player


class MarsEngine(MinimalEngine):

    #computes the current board value, positive = white has better position
    def board_value(board):    
        value=0

        #check if game is over
        res=board.outcome()
        if(not res.termination == None):
            if(res.termination ==1):
                if res.winner:
                    return 100000
                else:
                    return -100000  
            else:
                return 0
            

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
        
        

    def search(self, board: chess.Board, *args: HOMEMADE_ARGS_TYPE) -> PlayResult:
        
        moves=list(board.legal_moves)
        values=[]

        for move in moves:
            values.append([random.random(),move])
            if board.is_capture(move):
                values[-1][0]+=piece_values[board.piece_map()[move.to_square]]
            if (board.is_attacked_by(not board.turn, move.to_square)):
                values[-1][0]-=piece_values[board.piece_map()[move.from_square]]
            if (board.is_attacked_by(not board.turn , move.from_square)):
                values[-1][0]+=piece_values[board.piece_map()[move.from_square]]

            board.push(move)
            if(board.is_check):
                values[-1][0]+=50
            if(board.is_checkmate):
                values[-1][0]+=100000
            board.pop()


        values.sort(reverse=True)
        return PlayResult(values[0][1], None)



class RandomMove(ExampleEngine):
    """Get a random move."""

    def search(self, board: chess.Board, *args: HOMEMADE_ARGS_TYPE) -> PlayResult:  # noqa: ARG002
        """Choose a random move."""
        return PlayResult(random.choice(list(board.legal_moves)), None)


class Alphabetical(ExampleEngine):
    """Get the first move when sorted by san representation."""

    def search(self, board: chess.Board, *args: HOMEMADE_ARGS_TYPE) -> PlayResult:  # noqa: ARG002
        """Choose the first move alphabetically."""
        moves = list(board.legal_moves)
        moves.sort(key=board.san)
        return PlayResult(moves[0], None)


class FirstMove(ExampleEngine):
    """Get the first move when sorted by uci representation."""

    def search(self, board: chess.Board, *args: HOMEMADE_ARGS_TYPE) -> PlayResult:  # noqa: ARG002
        """Choose the first move alphabetically in uci representation."""
        moves = list(board.legal_moves)
        moves.sort(key=str)
        return PlayResult(moves[0], None)


class ComboEngine(ExampleEngine):
    """
    Get a move using multiple different methods.

    This engine demonstrates how one can use `time_limit`, `draw_offered`, and `root_moves`.
    """

    def search(self,
               board: chess.Board,
               time_limit: Limit,
               ponder: bool,  # noqa: ARG002
               draw_offered: bool,
               root_moves: MOVE) -> PlayResult:
        """
        Choose a move using multiple different methods.

        :param board: The current position.
        :param time_limit: Conditions for how long the engine can search (e.g. we have 10 seconds and search up to depth 10).
        :param ponder: Whether the engine can ponder after playing a move.
        :param draw_offered: Whether the bot was offered a draw.
        :param root_moves: If it is a list, the engine should only play a move that is in `root_moves`.
        :return: The move to play.
        """
        if isinstance(time_limit.time, int):
            my_time = time_limit.time
            my_inc = 0
        elif board.turn == chess.WHITE:
            my_time = time_limit.white_clock if isinstance(time_limit.white_clock, int) else 0
            my_inc = time_limit.white_inc if isinstance(time_limit.white_inc, int) else 0
        else:
            my_time = time_limit.black_clock if isinstance(time_limit.black_clock, int) else 0
            my_inc = time_limit.black_inc if isinstance(time_limit.black_inc, int) else 0

        possible_moves = root_moves if isinstance(root_moves, list) else list(board.legal_moves)

        if my_time / 60 + my_inc > 10:
            # Choose a random move.
            move = random.choice(possible_moves)
        else:
            # Choose the first move alphabetically in uci representation.
            possible_moves.sort(key=str)
            move = possible_moves[0]
        return PlayResult(move, None, draw_offered=draw_offered)
