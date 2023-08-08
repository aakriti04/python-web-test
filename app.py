from flask import Flask, render_template

import database

app = Flask(__name__)

data = [
  {
    'name': 'aakriti',
    'age': 25
  },
  {
    'name': 'abc',
    'age': 30
  },
  {
    'name': 'mno',
    'age': 45
  },
  {
    'name': 'xyz',
    'age': 45
  },
]

data1 = database
print(data)


@app.route("/")
def hello_world():
  # return "<p>Hello, World!</p>"
  return render_template('home.html', data=data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
