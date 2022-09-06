
from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='mydemo')
print('Successfully connected to Database')
cur = conn.cursor()

def home(request):
    return render(request, 'home.html')

def infolisting(request):
    cur.execute("SELECT * FROM 'tbl_user'")
    data = cur.fetchall()
    print(list(data))
    return render(request, 'view.html', {'info': data}) 

def infocreate(request):
    return render(request, 'add.html')

def infocreate(request):
    return render(request, 'add.html')   


def infoaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['txt1']
        cur.execute("INSERT INTO `tbl_user`(`user-id`) VALUES ('{}')".format(id))
        conn.commit()
        return redirect(infocreate) 
    else:
        return redirect(infocreate)

def infodelete(request,id):
    print(id)
    cur.execute("delete from `tbl_user` where `user_id` = {}".format(id))
    conn.commit()
    return render(request, 'edit.html')


