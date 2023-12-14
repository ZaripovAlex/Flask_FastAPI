# # Создать страницу, на которой будет форма для ввода текста и
# # кнопка "Отправить"
# # При нажатии кнопки будет произведен подсчет количества слов
# # в тексте и переход на страницу с результатом.
#
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.get('/')
# def index():
#     return render_template('form2.html')
#
# @app.post("/")
# def index_post():
#     text = request.form['text']
#     length = len(text.split())
#     return render_template("form2.html", text=text, length=length)
#
# if __name__ == '__main__':
#     app.run(debug=True)
