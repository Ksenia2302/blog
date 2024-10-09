from django.shortcuts import render, HttpResponse, redirect
from .models import New, User


def index(request):
    news = New.objects.all()

    return render(request, 'index.html', {'news': news})


def view(request, id):
    if request.method == 'POST':
        #данные приходят из формы добавления комментарий
        pass
    new = New.objects.filter(id=id).first()
    return render(request, 'view.html', {'new': new})


def contacts(request):
    return render(request, 'contacts.html')


def reg(request):
    suc = ''
    error = ''

    #обработка формы регистрации
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']

        if User.objects.filter(login=login).exists():
            error += 'Такой логин уже существует!'
        else:
            #добавление в модель User (регистрация)
            user = User()
            user.login = login
            user.password = password
            user.save()
            suc += 'Вы успешно зарегистрированы!'
    return render(request, 'reg.html', {'suc': suc, 'error': error})


def auth(request):
    error = ''
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']

        if User.objects.filter(login=login).filter(password=password).exists():
            request.session['login'] = login
        else:
            error += 'Логин и/или пароль error!'

    return render(request, 'auth.html',{'error': error})


def logout(request):
    if 'login' in request.session:
        del request.session['login']
    return redirect('/auth')