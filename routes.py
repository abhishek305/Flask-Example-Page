from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', the_title=' Home Page')



if __name__ == '__main__':
    app.run(debug=True)
