from flask import *
from calc import count
import sqlite3

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        error = None

        with sqlite3.connect("employee.db") as con:
            curp = con.cursor()
            user = curp.execute(
                "SELECT * FROM user WHERE username = ? and password = ?", (name, password,)
            ).fetchone()
            con.commit()

        if user is None:
            error = "Incorrect Username"
        elif user['password'] != password:
            error = "Incorrect password"
        else:
            return redirect(url_for('home'))
        # flash(error)
    return render_template("signin.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        error = None
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            with sqlite3.connect("employee.db") as con:
                curp = con.cursor()
                curp.execute("INSERT into user(name, email, password) values (?,?,?)", (name, email, password))
                con.commit()
        except:
            con.rollback()
            error = "we can not add the employee to the list"

        finally:
            con.close()
            # flash(error)
        return redirect(url_for('home'))
    return render_template("signup.html")


@app.route('/home', methods=["GET", "POST"])
def home():
    msg = None
    if request.method == "POST":
        num = request.form['number']
        check = count(int(num))
        if num is not None:
            if check:
                msg = num + " is an Armstrong number"
            else:
                msg = num + " is not an Armstrong number"
            return render_template("index.html", msg=msg)
    return render_template("index.html")


@app.route('/range',methods=["GET", "POST"])
def ranges():
    msg = None
    if request.method == "POST":
        num1 = request.form['num']
        num2 = request.form['num1']
        numbers = []
        x = 0
        if num1 is not None:
            for num in range(int(num1),int(num2)):
                check = count(int(num))
                if check:
                    numbers.append(num)
            if numbers:
                return render_template("range.html", numbers=numbers)
    return render_template("range.html")


if __name__ == "__main__":
    app.run(debug=True)
