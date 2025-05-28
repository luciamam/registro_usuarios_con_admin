from flask import Flask, redirect,render_template
from flask_bootstrap import Bootstrap4
from formularios.forms import RegisterForm,LoginForm
from dotenv import load_dotenv

load_dotenv()
import os




app=Flask(__name__)
Bootstrap4(app)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')



@app.route('/')
def inicio():
    return render_template('Home.html')


@app.route('/register')
def mostrar_register():
    form=RegisterForm()
    
    return render_template('Register.html',form=form)





@app.route('/login')
def mostrar_login():
    form=LoginForm()
    
    return render_template('Login.html',form=form)


@app.errorhandler(404)
def NotFound(mensaje):
    return render_template ('NotFound.html'),404











if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')

