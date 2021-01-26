#coding: UTF-8
# Importando as seguintes funcionalidades no módulo flask
from flask import Flask, render_template, request, redirect, url_for

# Importando o módulo (db) de Banco de Dados que contém as configurações de acesso ao nosso Banco de Dados e também estou importando o Drive Connector
import mysql.connector
import db

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

# Função ('register'), quando chamada retornará a página de formulário de cadastro para empresas
def register() -> 'html':
    return render_template('register.html',
                           the_title='MyBusiness - Register',
                           the_heading='Formulário de Cadastro')

# Decorador route, para o caminho web ('/registered') somente será quando o formulário for preenchido e clicar no botão Registrar
@app.route('/registered', methods=['GET', 'POST'])

# Função ('registered'), temos uma condição caso o método seja POST, basicamente, registra os dados ao sistema de Banco de Dados MySQL
def registered() -> 'str':
    if request.method == "POST":
        database = mysql.connector.connect(**db.DBconfig())
        cursor = database.cursor()

        _SQL = """INSERT INTO empresa
                  (razao_social, tipo, cnpj, estado, municipio, cep)
                  VALUES
                  (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (request.form['razao_social'],
                              request.form['tipo'],
                              request.form['cnpj'],
                              request.form['estado'],
                              request.form['municipio'],
                              request.form['cep'],))
        database.commit()
        cursor.close()
        database.close()

    return redirect(url_for('index'))

# Decorador route, para o caminho web ('/view'), é específico para visualizar todas as empresas cadastradas
@app.route('/view', methods=['GET'])

# Função ('view'), também temos uma condição, caso o método seja GET, vamos ativar nosso cursor() e dar execute() na consulta SQL que precisamos.
def view() -> 'html':
    if request.method == "GET":
        database = mysql.connector.connect(**db.DBconfig())
        cursor = database.cursor()

        # cursor.execute("SELECT * FROM empresa WHERE tipo = 'Matriz'") --- Estou selecionando na tabela empresa somente do tipo Matriz
        cursor.execute("SELECT * FROM empresa")

        empresa = cursor.fetchall()

        cursor.close()
        database.close()

        return render_template('view.html', empresa=empresa)

# Decorador route, para o caminho web ('remove/índice_do_id_empresa'), assim que é removido uma empresa cadastrada
@app.route('/remove/<int:id>')

# Função ('delete'), Ao fazer a conexão com o banco de dados, vamos fazer a consulta de exclusão c/ a cláusula WHERE
def delete(id):
    database = mysql.connector.connect(**db.DBconfig())
    cursor = database.cursor()

    _SQL = """DELETE FROM empresa
          WHERE id = %s"""

    cursor.execute(_SQL, (id,))

    empresa = cursor.fetchall()

    database.commit()
    cursor.close()
    database.close()

    return redirect(url_for('view', empresa=empresa))

#

if __name__ == '__main__':
    app.run(debug=True)
