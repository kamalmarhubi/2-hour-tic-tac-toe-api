from flask import abort
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
        board = Board(wire_format=request.args['board'])
    except ValueError:
        abort(400)  # inavlid board, bad request

    if Board.O not in board.next_players():
        # This catches an inva
        abort(400)  # not O's turn, bad request

    return board.wire_format()
