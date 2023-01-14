import pandas as pd

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print("Query executed successfully")

# массив имен докторов
def docName2(con,spec_list):
    ds = pd.read_sql('''select idDoctor, fullDocName, DS.Speciality
from Doctors
join DoctorSpeciality DS on DS.idDoctorSpeciality = Doctors.idDoctorSpeciality''',con)
    if spec_list:
        ds = ds[ds.ProcedureName.isin(spec_list)]
    return ds

# для рендера специализаций
def SpecName(con):
    return pd.read_sql(''' SELECT Speciality as Cпециальность from DoctorSpeciality''',con)

# cписок доков по заданной специальности
def docName(con,spec_id):
    return pd.read_sql(f''' SELECT fullDocName from Doctors
    where idDoctorSpeciality = {spec_id} ''', con)

# доктора по датам
def FindDocs(con,dateStart,dateEnd,doc):
    ds = pd.read_sql(f''' select idAttends, AttendDate as Дата, AttendTime as Время, idPatients as Запись, D.fullDocName as Имя, S.Speciality as Должность
from Attends
join DoctorSchedule DS on Attends.idDoctorSchedule = DS.idDoctorSchedule
join Doctors D on DS.idDoctor = D.idDoctor
join DoctorSpeciality S on D.idDoctorSpeciality = S.idDoctorSpeciality
where AttendDate >= '{dateStart}' and AttendDate <= '{dateEnd}' and D.fullDocName = '{doc}' ''',con)
    ds['Запись'] = ds['Запись'].fillna(0)
    return ds

# доктора по имени
def FindDocs2(con,doc):
    ds = pd.read_sql(f''' select idAttends, AttendDate as Дата, AttendTime as Время, idPatients as Запись, D.fullDocName as Имя, S.Speciality as Должность
    from Attends
    join DoctorSchedule DS on Attends.idDoctorSchedule = DS.idDoctorSchedule
    join Doctors D on DS.idDoctor = D.idDoctor
    join DoctorSpeciality S on D.idDoctorSpeciality = S.idDoctorSpeciality
    where  D.fullDocName = '{doc}' ''', con)
    ds['Запись'] = ds['Запись'].fillna(0)
    return ds

# добавить пациента
def addPat(con,val_name,val_age,val_gender,val_numPass):
    query = f'''INSERT INTO Patients (idPatients, fullName, age, gender, numPass)
VALUES ( null,'{val_name}', {val_age}, '{val_gender}', '{val_numPass}');'''
    execute_query(con,query)

# если есть пользователь вернет айдишник если нет добавит и вернет айдишник
def checkPat(con,val_name,val_age,val_gender,val_numPass):
    ds = pd.read_sql(f'''select * from Patients 
    where fullName = '{val_name}' and age = '{val_age}' and gender = '{val_gender}'
       and numPass = '{val_numPass}' ''',con)
    isempty = ds.empty
    if isempty:
        addPat(con,val_name,val_age,val_gender,val_numPass)
        print('добавил пацика')
    else:
        print('пацик уже есть')
    ds2 = pd.read_sql(f'''select idPatients from Patients
     where fullName = '{val_name}' and age = '{val_age}' and gender = '{val_gender}'
       and numPass = '{val_numPass}' ''',con)
    return ds2['idPatients'].values[0]

# добавить пациента по окошке(айди окошка)
def recPat(con,val_pat,diag_val,val_att):
    ds = f'''update Attends set idPatients = '{val_pat}', Diagnosis = '{diag_val}' where idAttends = '{val_att}' 
    '''
    execute_query(con,ds)

def get_id(con,dname):
    ds = pd.read_sql(f'''select idDoctor from Doctors where fullDocName = '{dname}' 
    ''',con)
    print(ds)

    return ds['idDoctor'].values[0]

def add_schedule(con,docid,dateval):
    ds = f'''insert into DoctorSchedule(idDoctor,VisitDate)
     values ('{docid}', '{dateval}'); '''
    execute_query(con,ds)
