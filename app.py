from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def projects(name):
    return 'Hello ' + name

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin():
    return redirect(url_for('index'))

@app.route("/api/data")
def get_data():
    return app.send_static_file("./data/data.json")

if __name__ == '__main__':
    app.run(debug=True)