from flask import Flask, render_template, request
from entities.palindrome import Palindrome
from entities.money import Money
from entities.animal import Animal
from entities.rifa import Rifa


app = Flask(__name__)

#Esta sera la ruta index (de la pagina principal)


@app.route('/palindrome', methods=['GET', 'POST']) 
def palindrome():
    
    if request.method == 'POST':
        phrase = request.form.get('input_phrase', '') #el punto get agarra el name del objeto html, no el id, el segundo parametro es para decir que se hace si no se encuentra lo del primer parametro
        
        p = Palindrome(phrase)
        
        resultado = p.is_palindrome()
        
        
        return render_template('result.html', resultado=resultado) #El segundo parametro es la funcion que esta esperando la vista renderizada
    return render_template('palindrome.html')

@app.route('/money', methods=['GET', 'POST'])
def money():
    
    if request.method == 'POST':
        
        cantidad = request.form.get('input_money', '')
        
        m = Money(cantidad)
        
        resultado = m.convertir()
        
        return render_template('result-money.html', resultado=resultado)
    return render_template('money.html')
    
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/azulejos')
def azulejos():
    return render_template('azulejos.html')

@app.route('/animals')
def animals():
    return render_template('animals.html', animals=Animal.get_list())

@app.route('/examen',methods=['GET', 'POST'])
def examen():
    if request.method == 'POST':
        numeros = []
    
        numeros.append(request.form.get('input_number1'))
        numeros.append(request.form.get('input_number2'))
        numeros.append(request.form.get('input_number3'))

        n = Rifa(numeros)
        
        result = n.sortear()[0]
        numero_ganador = n.sortear()[1]
        
        return render_template('result-examen.html', result=result, numeros = numeros, numero_ganador=numero_ganador)
        
    return render_template('examen.html')

if __name__ == '__main__':
    app.run(port=5069, host='0.0.0.0') #Port sirve para cambiar manualmente el puerto que usa la app, default = 5000
                                        #host es para decirle a la app que se pueda acceder de cualquier direccion