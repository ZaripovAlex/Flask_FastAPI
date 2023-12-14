# # Создать страницу, на которой будет форма для ввода логина и пароля,
# # при нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход
# # на страницу приветствия пользователя или страницу с ошибкой.
#
#
# from flask import Flask, request, render_template, redirect, url_for
#
# app = Flask(__name__)
#
#
# @app.get("/")
# def index():
#     return render_template("login_form.html")
#
#
# @app.post('/login/')
# def login():
#     login = request.form['username']
#     password = request.form['password']
#     user_data = {"123": ("admin", "111")}
#     if (login, password) not in user_data.values():
#         print("invalid username or password")
#         return redirect(url_for('index'))
#     return redirect(url_for('login_success', name=login))
#
#
# @app.route('/success/<name>')
# def login_success(name: str):
#     return render_template("name.html", context=name)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
