# # Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# # Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# # Данные о студентах должны быть переданы в шаблон через контекст.
#
# from flask import Flask, render_template
#
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     context = [
#         {
#             "name": "Иван",
#             "last_name": "Петров",
#             "age": 24
#         },
#         {
#             "name": "Петр",
#             "last_name": "Иванов",
#             "age": 34
#          },
#         {
#             "name": "Анна",
#             "last_name": "Смирнова",
#             "age": 23
#          },
#         {
#             "name": "Дмитрий",
#             "last_name": "Яшин",
#             "age": 29
#          },
#         {""
#             "name": "Яков",
#             "last_name": "Дмитриев",
#             "age": 42
#          }
#     ]
#     return render_template("table.html",context=context)
#
# if __name__ == '__main__':
#     app.run(debug=True)