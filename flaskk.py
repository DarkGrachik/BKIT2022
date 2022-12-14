from flask import Flask
from Fibonachi import Fibonachi

app = Flask(__name__)

@app.route('/')
def title():
    return "<p>Функция Фибоначи (наверно)<p>"

@app.route('/<int:n>')
def number(n):
    fibonachi_gen = Fibonachi(n)
    res = [next(fibonachi_gen) for i in range(n)]
    return res

@app.errorhandler(404)
def not_found_error(error):
    return "Введите целое число, а не непонятно что"


if __name__ == "__main__":
    app.run(debug = True)
