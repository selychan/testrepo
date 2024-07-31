from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ""
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('index.html', name=name)
    
@app.route('/hello', methods=['GET', 'POST'])
def index():
    name = "hello it's means merhaba in turkish."
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
