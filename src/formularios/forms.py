from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField,PasswordField
from wtforms.validators import DataRequired,Length, EqualTo ,Email




class RegisterForm(FlaskForm):
    name=StringField('Introduce tu nombre', validators=[DataRequired(),Length(min=4,max=12)])
    email=EmailField('introduce un correo electronico',validators=[DataRequired(),Length(min=4,max=12),Email()])
    password=PasswordField('Introduce una contraseña', validators=[DataRequired(),Length(min=4,max=12),EqualTo('confirm')])
    confirm=PasswordField('Introduce una contraseña', validators=[DataRequired(),Length(min=4,max=12)])
    submit=SubmitField('Registrarse')



class LoginForm(FlaskForm):
    email=EmailField('introduce un correo electronico',validators=[DataRequired(),Length(min=4,max=12),Email()])
    password=PasswordField('Introduce una contraseña', validators=[DataRequired(),Length(min=4,max=12)])
    submit=SubmitField('iniciar Sesion ')
    
