from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/playlist')
def playlist():
    return render_template('playlist.html')

@app.route('/modules')
def modules():
    return render_template('modules.html')
if __name__ == '__main__':
    app.run(debug=True)
