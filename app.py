from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("churn.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        f1 REAL, f2 REAL, f3 REAL, f4 REAL,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------- LOGIN ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect("churn.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = u
            session["role"] = user[3]

            if user[3] == "admin":
                return redirect("/admin")
            return redirect("/index")
        else:
            return "Invalid login"

    return render_template("login.html")


# ---------- REGISTER ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect("churn.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)", (u, p, "user"))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("register.html")


# ---------- PREDICT ----------
@app.route("/index", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect("/")

    result = ""

    if request.method == "POST":
        try:
            f1 = float(request.form["f1"])
            f2 = float(request.form["f2"])
            f3 = float(request.form["f3"])
            f4 = float(request.form["f4"])

            total = f1 + f2 + f3 + f4

            if total > 200:
                result = "Customer Will Leave"
            else:
                result = "Customer Will Stay"

            conn = sqlite3.connect("churn.db")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO history(username,f1,f2,f3,f4,result) VALUES(?,?,?,?,?,?)",
                (session["user"], f1, f2, f3, f4, result),
            )
            conn.commit()
            conn.close()

        except:
            result = "Enter valid numbers"

    return render_template("index.html", result=result)


# ---------- HISTORY ----------
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/")

    conn = sqlite3.connect("churn.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM history WHERE username=?", (session["user"],))
    data = cur.fetchall()
    conn.close()

    return render_template("history.html", data=data)


# ---------- ADMIN ----------
@app.route("/admin")
def admin():
    if "user" not in session or session["role"] != "admin":
        return redirect("/")

    conn = sqlite3.connect("churn.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM history")
    data = cur.fetchall()
    conn.close()

    return render_template("admin.html", data=data)


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

    