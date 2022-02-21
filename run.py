import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["get"])
def show_pages():
    return render_template('index.html')

@app.route('/player')
def show_player():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'playbutton.jpg', mimetype='image/vnd.microsoft.icon')

@app.route('/play')
def sound():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'work.m4a', mimetype='audio/m4a')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=4999)