from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection


@app.route('/hh', methods=['get'])

def hh():
    html = render_template('hh.html')
    return html