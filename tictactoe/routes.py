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
    board = Board(wire_format=request.args['board'])

    return board.wire_format()
