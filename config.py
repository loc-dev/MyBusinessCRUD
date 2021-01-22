# Importando as seguintes funcionalidades no módulo flask

from flask import Flask, render_template

# Criando objeto Flask, atribuir para uma variável (app)

app = Flask(__name__)

# Aqui teremos nosso decorador route, é próprio do Flask, através da variável (app)
# Logo, temos nosso caminho web ('/index') que está associada a função ('index')
@app.route('/index')

# Função ('index'), quando chamada retornará o HTML para o servidor web.
def index() -> 'html':
    return render_template('index.html')

app.run()
