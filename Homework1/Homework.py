# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/men/')
def men_s_clothing():
    return render_template("men.html")

@app.route('/women/')
def women_s_clothing():
    return render_template("women.html")

@app.route('/kids/')
def kids_clothing():
    return render_template("kids.html")

if __name__ == '__main__':
    app.run(debug=True)
