from tictactoe import app


@app.route("/healthz")
def healthz():
    """Health check endpoint."""

    return 'ok'
