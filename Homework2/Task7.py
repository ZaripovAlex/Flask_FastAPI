# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template( 'form1.html')

@app.post('/')
def index_post():
    number = int(request.form['number'])
    print(number)
    text = f"Вы ввели число {number}. Квадрат этого числа {number**2}"
    return render_template('result2.html', text=text)



if __name__ == '__main__':
    app.run(debug=True)