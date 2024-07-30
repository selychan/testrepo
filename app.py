from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ""
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('index.html', name=name)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    greeting = ""
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            greeting = f"Hello, {name}!"
        else:
            greeting = "Hello, stranger!"
    return greeting
if __name__ == '__main__':
    app.run(debug=True)
