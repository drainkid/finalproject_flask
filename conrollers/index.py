from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.index_model import SpecName

@app.route('/', methods=['get'])
def index():
    conn = get_db_connection()
    df_spec = SpecName(conn)
    specval = request.values.get('docbutton')

    if specval:
        spec_id = request.values.get('speciality')
        session['speciality'] = spec_id
        if session['speciality'] is not None:
            return redirect(url_for('doctors'))
        else:
            session['speciality'] = 0

    elif request.values.get('datebutton'):
        spec_id = request.values.get('speciality')
        session['speciality'] = spec_id
        if session['speciality'] is not None:
            return redirect(url_for('date'))
        else:
            session['speciality'] = 0

    html = render_template(
        'index.html',
    len = len,
    relation = df_spec
    )
    return html
