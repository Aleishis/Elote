from flask import Flask, render_template, request
from entities.palindrome import Palindrome


app = Flask(__name__)

#Esta sera la ruta index (de la pagina principal)


@app.route('/palindrome', methods=['GET', 'POST']) 
def palindrome():
    
    if request.method == 'POST':
        phrase = request.form.get('input_phrase', '') #el punto get agarra el name del objeto html, no el id, e; segundo parametro es para decir que se hace si no se encuentra lo del primer parametro
        
        p = Palindrome(phrase)
        
        resultado = p.is_palindrome()
        
        
        return render_template('result.html', resultado=resultado) #El segundo parametro es la funcion que esta esperando la vista renderizada
    return render_template('palindrome.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/azulejos')
def azulejos():
    return render_template('azulejos.html')

if __name__ == '__main__':
    app.run(port=5069, host='0.0.0.0') #Port sirve para cambiar manualmente el puerto que usa la app, default = 5000
                                        #host es para decirle a la app que se pueda acceder de cualquier direccion