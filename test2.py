from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/vulnerable')
def vulnerable_view():
    user_input = request.args.get('user_input', '')
    response_html = f"<html><body>User input: {user_input}</body></html>"
    return response_html

if __name__ == '__main__':
    app.run(debug=True)

app.run(host="0.0.0.0")
