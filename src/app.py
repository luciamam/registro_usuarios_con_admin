from flask import Flask, redirect,render_template,request,redirect,url_for,flash
from flask_bootstrap import Bootstrap4
from formularios.forms import RegisterForm,LoginForm
from dotenv import load_dotenv
from werkzeug.security import check_password_hash,generate_password_hash
from datetime import datetime,UTC

load_dotenv()
import os
#  ahora vamos a introduci mongodb 

from pymongo import MongoClient



app=Flask(__name__)
Bootstrap4(app)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
client = MongoClient("mongodb://localhost:27017/")
db=client['registros_usuarios_con_admin']
usuarios=db['usuarios']




@app.route('/')
def inicio():
    return render_template('Home.html')


@app.route('/register')
def mostrar_register():
    form=RegisterForm()
    
    return render_template('Register.html',form=form)


@app.route('/register',methods=['POST'])
def registrarse():
    datos=request.form
    name=datos['name']
    email=datos['email']
    password=datos['password']
    usuario={
            "name":name,
            "email":email,
            "password":generate_password_hash(password),
            "fecha":datetime.now(UTC)
            }
            # estamos insertando aqui el usuario 
    db.usuarios.insert_one(usuario)
    return redirect(url_for('perfil'))
    







@app.route('/login')
def mostrar_login():
    form=LoginForm()
    
    return render_template('Login.html',form=form)


@app.route('/login',methods=['POST'])
def iniciar_sesion():
    datos=request.form
    email=datos['email']
    password=datos['password']

    usuario=db.usuarios.find_one({"email":email})
    print("el usuario",usuario)
    if usuario:
        if check_password_hash(usuario['password'],password):
            return redirect(url_for('perfil'))
        else:
            flash("contraseña incorrecta","info")
            return  redirect(url_for('mostrar_login'))

    else:
        flash("usario no existe ","danger")
        return  redirect(url_for('mostrar_login'))




@app.route('/perfil')
def perfil():
    return render_template('Perfil.html')


@app.errorhandler(404)
def NotFound(mensaje):
    return render_template ('NotFound.html'),404











if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')

