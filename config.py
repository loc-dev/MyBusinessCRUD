# Importando as seguintes funcionalidades no módulo flask

from flask import Flask, render_template, request, redirect, url_for

# Importando o driver de Banco de Dados
import mysql.connector

# Criando objeto Flask, atribuir para uma variável (app)
app = Flask(__name__)

# Aqui teremos nosso decorador route, é próprio do Flask, através da variável (app)
# Logo, temos nosso caminho web ('/') que será uma forma para redirecionamento ao ('/index') que está associada a função ('index')
@app.route('/')
@app.route('/index')

# Função ('index'), quando chamada retornará o HTML para o servidor web
def index() -> 'html':
    return render_template('index.html',
                           the_title='MyBusiness - Painel',
                           the_heading='Painel Administrativo')

# Decorador route, para o caminho web ('/register')
@app.route('/register')

# Função ('Registrar'), quando chamada retornará a página de formulário de cadastro para empresas
def register() -> 'html':
    return render_template('register.html',
                           the_title='MyBusiness - Register',
                           the_heading='Formulário de Cadastro')

# Decorador route, para o caminho web ('/registered') somente será quando o formulário for preenchido e clicar no botão Registrar
@app.route('/registered', methods=['GET', 'POST'])

# Função ('Registrado'), temos uma condição caso o método seja POST, basicamente, registra os dados ao sistema de Banco de Dados MySQL
def registered() -> 'str':
    if request.method == "POST":
        dbconfig = { 'host': '127.0.0.1',
                     'user': 'admin',
                     'password': '123456',
                     'database': 'mybusinesslogDB', }

        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()

        _SQL = """insert into empresa
                  (razao_social, tipo, cnpj, estado, municipio, cep)
                  values
                  (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (request.form['razao_social'],
                              request.form['tipo'],
                              request.form['cnpj'],
                              request.form['estado'],
                              request.form['municipio'],
                              request.form['cep'],))
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
