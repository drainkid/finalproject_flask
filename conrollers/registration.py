from werkzeug.security import generate_password_hash

from app import app
from flask import render_template, request, flash

from models.index_model import create_user
from utils import get_db_connection


@app.route("/registration", methods=['POST', "GET"])
def registration():
    if request.method == "POST":
        if len(request.form["password1"]) > 4 and len(request.form["login"]) > 4 and \
                request.form["password1"] == request.form["password2"]:
            hash = generate_password_hash(request.form["password1"])
            conn = get_db_connection()
            res = create_user(conn, request.form["login"], hash)
            if res:
                flash("Вы успешно зарегестрированы", "success")
            else:
                flash("Ошибка добавления в бд", "error")
        else:
            flash("Неверно заполнены поля", "error")
    return render_template("registration.html")
