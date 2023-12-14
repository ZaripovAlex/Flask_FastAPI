# # Создать страницу, на которой будет кнопка "Нажми меня",
# # при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.
#
# from flask import Flask, url_for, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     data = {"name": "Alex"}
#     return render_template("button.html", **data)
#
# @app.route('/greet/<name>')
# def greet(name):
#     return render_template("name.html", context=name)
#
# if __name__ == '__main__':
#     app.run(debug=True)