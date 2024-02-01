from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # List of games
    games = [
        'Atlas.py', 'Chess.py', 'Hangman.py', 'Maze.py', 'MindGuess Prodigy.py',
        'Rockin\' Paper Scissors.py', 'Sudoku.py', 'Text Based Puzzle Game.py',
        'Trivia Tornado.py', 'Word Blitz.py', 'Word Whisler.py',
        'snakes and ladders.py', 'tictactoe.py'
    ]
    return render_template('index.html', games=games)

@app.route('/play/<game_name>')
def play_game(game_name):
    # Assuming the game name corresponds to the file in the SRC directory
    return redirect(url_for('static', filename=f'./SRC/{game_name}'))

if __name__ == '__main__':
    app.run(debug=True)
