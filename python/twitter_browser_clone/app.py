from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

buzzes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        buzz = request.form['buzz']
        buzzes.append(buzz)
        return redirect(url_for('index'))
    return render_template('index.html', buzzes=buzzes)

if __name__ == '__main__':
    app.run(debug=True)

