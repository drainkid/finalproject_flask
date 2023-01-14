import pandas as pd

from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import FindDocs,FindDocs2,docName, get_id,add_schedule

def convert(date):
    dates=date.split('.')
    if(len(dates)>3):
        return dates[2]+'-'+dates[1]+'-'+dates[0]
    else:
        return date

@app.route('/date', methods=['get'])

def date():
    conn = get_db_connection()
    a = int(session.get('speciality'))
    df_docs = docName(conn,a)
    date_df = None # деф дата фрейм
    date_list = [] # массив дат
    doc_list = list(df_docs['fullDocName']) # массив доков по должности выбранной
    print(doc_list)
    gdate_list = [] # массив из уникальных дат

    if request.values.get('submitGetDate'):
        startDate = request.values.get('dateStart')
        endDate = request.values.get('dateEnd')
        startDate = convert(startDate)
        endDate = convert(endDate)
        for elem in doc_list:
            date_list_df = FindDocs(conn, startDate, endDate, elem)
            date_list.append(date_list_df)

        if date_list:
            for elem in date_list:
                df_Date_record_uniq_date = elem.Дата.unique()
                gdate_list.append(df_Date_record_uniq_date)
            # print('huy', gdate_list)

    if request.values.get('subdocname'):
        docidd = get_id(conn,request.values.get('docname'))
        print('aidi ', docidd)
        add_schedule(conn,docidd,convert(request.values.get('datedoc')))


    html = render_template(
        'date.html',
        len=len,
        int=int,
    relation = date_list,
    randchar = gdate_list)
    return html