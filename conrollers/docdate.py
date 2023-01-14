from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import docName, FindDocs2


@app.route('/docdate', methods=['get'])

# посмотреть
def docdate():
    conn = get_db_connection()
    uniq_date_list = []

    if request.values.get('doctors'):
        dlist = []
        doc_list = request.values.getlist('doctors')
        for elem in doc_list:
            df_fdoc = FindDocs2(conn ,elem)
            dlist.append(df_fdoc)
            print(dlist)
    else:
        dlist = []
        doc_list = []

    if doc_list:
        for elem in dlist:
            specval = elem.Дата.unique()
            uniq_date_list.append(specval)

    html = render_template(
        'docdate.html',
        relation=dlist,
        len=len,
        int=int,
        randchar=uniq_date_list)
    return html
