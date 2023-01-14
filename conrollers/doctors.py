from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.index_model import docName, FindDocs2


@app.route('/doctors', methods=['get'])

def doctors():
    conn = get_db_connection()
    a = session.get('speciality')
    df_doc= docName(conn,a)

    html = render_template(
        'doctors.html',
        len=len,
        relation=df_doc
    )

    return html