from flask import Flask, render_template

app = Flask(__name__)


usuarios = {
    'Jessenia': 25,
    'Carlos': 30
}

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/user')
def user():
    
    return render_template('user.html', usuariosHtml=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
