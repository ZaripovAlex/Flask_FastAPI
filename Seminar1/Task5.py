# # Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".
#
# from flask import Flask
#
# app = Flask(__name__)
# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Моя первая страница</title>
# </head>
# <body>
#     <p>HELLO WORLD!</p>
# </body>
# </html>
# """
# @app.route('/')
# def index():
#     return html
#
# if __name__ == '__main__':
#     app.run(debug=True)