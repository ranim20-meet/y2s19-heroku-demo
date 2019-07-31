from flask import Flask, render_template
app = Flask(__name__)

opposite_day = False
@app.route('/')
def home_page():
    foods = ["Sushi", "Pasta", "Steak", "Sweets", "sondos"]
    least_foods = ["Brussels sproute", "Onion", "Spicy things", "Ariel: fish", "Yuval K: Hummus"]
    return render_template("index.html", foods = foods, least_foods = least_foods, opposite_day = opposite_day)

if __name__ == '__main__':
   app.run(debug = True)