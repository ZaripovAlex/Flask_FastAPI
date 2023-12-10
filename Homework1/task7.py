# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = [
            {
                "title": "Новость 1",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus consequuntur doloribus impedit optio vitae? Blanditiis culpa minima quae quam totam.",
                "release": "10.12.2023"
            },
            {
                "title": "Новость 2",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus consequuntur doloribus impedit optio vitae? Blanditiis culpa minima quae quam totam.",
                "release": "09.12.2023"
             },
            {
                "title": "Новость 3",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus consequuntur doloribus impedit optio vitae? Blanditiis culpa minima quae quam totam.",
                "release": "08.12.2023"
             },
            {
                "title": "Новость 4",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus consequuntur doloribus impedit optio vitae? Blanditiis culpa minima quae quam totam.",
                "release": "07.12.2023"
             },
            {
                "title": "Новость 5",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus consequuntur doloribus impedit optio vitae? Blanditiis culpa minima quae quam totam.",
                "release": "06.12.2023"
             }
        ]
    return render_template( "news.html", context=context)

if __name__ == '__main__':
    app.run(debug=True)