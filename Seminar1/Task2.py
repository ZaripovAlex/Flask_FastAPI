# # Добавьте две дополнительные страницы в ваше веб-приложение: страницу "about" и страницу "contact".
#
# from flask import Flask
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'Hello, World!'
#
# @app.route('/about/')
# def about():
#     return 'That\'s page about company'
#
#
# @app.route('/contact/')
# def contact():
#     return 'Our contacts: company@mail.com'
#
#
# if __name__ == "__main__":
#     app.run(debug=True)