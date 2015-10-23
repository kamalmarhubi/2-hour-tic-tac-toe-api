from flask import abort
from flask import make_response
from flask import request

from tictactoe import app
from tictactoe.board import Board


@app.route("/healthz")
def healthz():
    """Health check endpoint."""

    return 'ok'


@app.route("/game")
def game():
    """Endpoint for the assignment."""

    # KeyError type from the args dict results in HTTP 400.
    # For details, see
    #  http://werkzeug.pocoo.org/docs/0.10/datastructures/#werkzeug.datastructures.MultiDict

    try:
        # TODO: overly broad try / except
        board = Board(wire_format=request.args['board'])

        if Board.O not in board.next_players():
            abort(400)  # not O's turn, bad request

        # Simply attempt the first move returned by available moves.
        board.make_move(Board.O, board.available_moves(Board.O)[0])

        resp = make_response(board.wire_format())
        resp.mimetype = 'text/plain'

        return resp

    except ValueError:
        abort(400)  # inavlid board, bad request
