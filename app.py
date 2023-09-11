from flask import Flask, render_template, request, redirect, url_for
import jinja2.exceptions
import werkzeug.exceptions


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def huis():
    return render_template('home.html')


@app.route('/options', methods=['POST', 'GET'])
def opties():
    opties =[]
    # try:
    if request.method == 'POST':
        # upfile = request.files("file")
        # file = upfile.filename
        name = request.form.get("name")
        mail = request.form.get("email")

        # opties.append(file)
        opties.append(name)
        opties.append(mail)
        print(opties)

        return render_template("result.html", vnaam=name, email=mail)
        # return render_template("result.html", lijst=file, naam=mail)
        # return render_template("options.html")
    else:
        return render_template("options.html")


@app.route('/info')
def informatie():
    return render_template('info.html')


@app.route('/result')
def resultaten():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
