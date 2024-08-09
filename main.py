from flask import Flask
import random

app = Flask(__name__)

facts = [
   "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
   "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
   "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента."
]


coins = [
    "3 - Ты выиграл!",
    "2 - Ничья!",
    "1 - Увы, ты проиграл!"
]



@app.route("/")
def index():
    return "<h1>Добро Пожаловать!</h1>"


@app.route("/about")
def endpoint_about():
    return "<h1>Я программист!</h1>"


@app.route("/going")
def endpoint_going():
    return "<h1>Я люблю гулять!</h1>"


@app.route("/fact")
def endpoint_fact():
    return f"<h2>{random.choice(facts)}</h2>"
    

@app.route("/coin")
def endpoint_coin():
    return f"<h2>{random.choice(coins)}</h2>"

@app.route("/name")
def endpoint_name():
    return "<h2>Меня зовут Фёдор.</h2>"


if __name__ == "__main__":
    app.run(debug=True)
    
