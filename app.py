from flask import Flask, render_template


app = Flask(__name__)

#Esta sera la ruta index (de la pagina principal)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math')
def math():
    return render_template('math.html')

if __name__ == '__main__':
    app.run(port=5069, host='0.0.0.0') #Port sirve para cambiar manualmente el puerto que usa la app, default = 5000
                                        #host es para decirle a la app que se pueda acceder de cualquier direccion