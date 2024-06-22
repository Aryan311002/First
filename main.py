from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="HomePage")

@app.route('/welcome/<name>')
def welcome(name):
    return f"{name}"

@app.route("/name/<int:num>")
def info(name,num):
    if num<30:
        # Redirect to failed page
        return redirect(url_for('fail', sname=name, marks=num))
    else:
        # Redirect to passed page
        return redirect(url_for('passed', sname=name, marks=num))

@app.route('/passed/<sname>/<int:marks>')
def passed(sname, marks):
    return f'<h3>Congrats {sname.title()} Your marks is {marks}! You passed</h3>'

@app.route('/fail/<sname>/<int:marks>')
def fail(sname,marks):
    return f'<h2>Sorry {sname.title()} your marks is {marks}! you Failed</h2>'


@app.route("/about")
def about():
    return render_template("about.html", title="About Page")



if __name__ == "__main__":
    app.run(debug=True)
