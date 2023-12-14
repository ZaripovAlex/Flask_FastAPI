# # Создать страницу, на которой будет изображение и ссылка на другую страницу,
# # на которой будет отображаться форма для загрузки изображений.
#
# from flask import  Flask, request, render_template, redirect, url_for
#
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/form", methods=["GET"])
# def form_get():
#     return render_template("form.html")
#
# @app.route("/form", methods=["POST"])
# def form_post():
#     image = request.files.get('file')
#
#     return redirect(url_for("index"))
#
# if __name__ == '__main__':
#     app.run(debug=True)