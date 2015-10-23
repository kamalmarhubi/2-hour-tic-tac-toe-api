from tictactoe import app


if __name__ == '__main__':
    import sys
    debug = False
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'DEV'
    app.run(debug=debug)
