from flask import Flask, redirect,render_template






app=Flask(__name__)



@app.route('/')
def inicio():
    return "soy la tuta raiz"


@app.route('/register')
def mostrar_register():
    return "soy la ruta register"

    # return render_template('Regsiter.html')





@app.route('/login')
def mostrar_login():
    return "soy la ruta login "
    # return render_template('Login.html')


@app.errorhandler(404)
def NotFound(mensaje):
    return render_template ('NotFound.html'),404











if __name__=='__main__':
    app.run(debug=True)

