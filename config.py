# Importando as seguintes funcionalidades no módulo flask

from flask import Flask, render_template, request

# Criando objeto Flask, atribuir para uma variável (app)

app = Flask(__name__)

# Aqui teremos nosso decorador route, é próprio do Flask, através da variável (app)
# Logo, temos nosso caminho web ('/index') que está associada a função ('index')
@app.route('/')
@app.route('/index')

# Função ('index'), quando chamada retornará o HTML para o servidor web
def index() -> 'html':
    return render_template('index.html',
                           the_title='MyBusiness - Painel',
                           the_heading='Painel Administrativo')

@app.route('/register')

# Função ('Registrar'), quando chamada retornará a página de formulário de cadastro para empresas
def register() -> 'html':
    return render_template('register.html',
                           the_title='MyBusiness - Register',
                           the_heading='Formulário de Cadastro')

@app.route('/registered', methods=['GET', 'POST'])


def registered() -> str:
    if request.method == 'POST':
        razao_social = request.form.get['razao_social']
        tipo = request.form.get['tipo']
        cnpj = request.form.get['cnpj']
        estado = request.form.get['estado']
        municipio = request.form.get['municipio']
        cep = request.form.get['cep']

if __name__ == '__main__':
    app.run(debug=True)
