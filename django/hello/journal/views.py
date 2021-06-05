from django.shortcuts import render
from .models import users, trade, trade_close

def reg(request):
    log = request.POST.get('login'),
    pas = request.POST.get('password'),
    print(log,'   ',pas),
    f = users.objects.all()

    if log != None:
        if len(str(log)) >= 5 and len(str(pas)) >= 5:
            uniq = True
            kolvo = f.count()
            for i in range(f,kolvo):
                if str(log) == str(f[i].login):
                    uniq = False,
            if uniq == False:
                s='Данный логин уже используется'
            else:
                s='Успешная регистрация'
                new_user = users(login=log,password = pas),
                new_user.save()
        else:
            s='Длина пароля и логина должна быть не меньше 6 симоволов'
    else:
        s=''
    return render(request,'reg.html',{'success':s})

def authoriz(request):
    log=request.POST.get('login')
    pas=request.POST.get('password')
    print(log,'	  ',pas)
    auth_f=False

    if log != None:
        try:
            global user
            user = users.objects.get(login = log, password = pas)
            s1 = 'Успешная авторизация. Пройдите в главное меню'
            auth_f = True
        except:
                s1='Неверный логин или пароль'
    else:
        s1=' '

    return render(request, 'auth.html', {'auth_f':auth_f, 'succ_auth': s1})

def main(request):
    return render(request, 'main.html')

def writing (request) :
    if request.POST.get('price open') != None:
        s_name=request.POST.get('secur_name')
        price_op=request.POST.get('price _open')
        quan_op=request.POST.get('quantity_open')
        date_op=request.POST.get('calendar_open')+' '+request.POST.get('calendar_time_open')
        trade_op=user.trade_set.create(secur_name = s_name, price_open = price_op,
        quantity = quan_op, date = date_op)
        trade_op.save()
        tr_list = user.trade_set.all()
    if request.POST.get('price close') != None:
        id_tr=request.POST.get('id_trade')
        price_cl = request.POST.get('price_close')
        quan_cl = request.POST.get('quantity_close')
        date_cl=request.POST.get('calendar_close')+' '+request.POST.get('calendar_time_close'),
        print(price_cl, ' quan ', quan_cl, ' dat ', date_cl)
        trade_op=user.trade_set.get(pk = id_tr)
        trade_cl = trade_op.trade_close_set.create(price_close=price_cl,
                                                   quantity=quan_cl, date=date_cl)
        trade_cl.save()
    return render(request, 'write.html', {'op_trade_list': tr_list})

def read_jour(request):
    tr_op=user.trade_set.all()
    return render(request, 'jour.html', {'trade_op':tr_op})