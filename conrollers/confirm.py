from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.index_model import recPat, checkPat


@app.route('/confirm', methods=['get'])
def confirm():
    conn = get_db_connection()

    if request.values.get('record_button'):
        session['record'] = request.values.get('record_button')

    # добавляет пациентов при любом отличии данных
    if request.values.get('submitSuccess'):
        idpat = checkPat(conn, request.values.get('username'), request.values.get('age'),
                         request.values.get('gender'), request.values.get('numPass'))
        print(idpat)
        recPat(conn, idpat, request.values.get('diagnosis'), session['record'])
        return redirect(url_for('hh'))
    else:
        print('dolb')

    html = render_template('confirm.html')
    return html
