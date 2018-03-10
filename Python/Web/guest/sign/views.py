from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sign.forms import AddEventForm, AddGuestForm


# Create your views here.
def index(request):
    return render(request, "index.html")


# 登录动作
def login_action(request):
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return render(request, "index.html", {"error": "username or password null"})
        else:
            user = auth.authenticate(username=login_username, password=login_password)
            if user is not None:
                auth.login(request, user)  # 登录
                response = HttpResponseRedirect('/event_manage/')
                # response.set_cookie('user', username, 3600)     # 添加浏览器cookie
                request.session['user'] = login_username  # 将session信息记录到浏览器
                return response
            else:
                return render(request, 'index.html', {'error': 'username or password error!'})
    else:
        return render(request, "index.html")


# 发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {"user": username,
                                                 "events": event_list})


# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    new_search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=new_search_name)
    return render(request, 'event_manage.html', {"user": username,
                                                 "events": event_list})


# 添加发布会
def add_event(request):
    username = request.session.get('user', '')

    if request.method == 'POST':
        form = AddEventForm(request.POST)  # form包含提交的数据
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            limit = form.cleaned_data['limit']
            start_time = form.cleaned_data['start_time']
            status = form.cleaned_data['status']
            if status is True:
                status = 1
            else:
                status = 0

            Event.objects.create(name=name, limit=limit, address=address, status=status,
                                 start_time=start_time)
            return render(request, "add_event.html", {"user": username,
                                                      "form": form,
                                                      "success": "添加发布会成功！"})
    else:
        form = AddEventForm

    return render(request, "add_event.html", {"user": username, "form": form})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    pageinator = Paginator(guest_list, 3)
    page = request.GET.get('page')
    try:
        contacts = pageinator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = pageinator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面
        contacts = pageinator.page(pageinator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


# 添加嘉宾
def add_guest(request):
    username = request.session.get("user", "")

    if request.method == 'POST':
        form = AddGuestForm(request.POST)

        if form.is_valid():
            event = form.cleaned_data('event')
            realname = form.cleaned_data('realname')
            phone = form.cleaned_data('phone')
            email = form.cleaned_data('email')
            sign = form.cleaned_data('sign')
            if sign is True:
                sign = 1
            else:
                sign = 0

            Guest.objects.create(event=event, realname=realname, phone=phone, email=email, sign=sign)
            return render(request, "add_guest.html", {"user": username,
                                                      "form": form,
                                                      "success": "添加嘉宾成功！"})
    else:
        form = AddGuestForm
    return render(request, "add_guest.html", {"user": username, "form": form})


# 嘉宾搜索
@login_required
def search_phone(request):
    username = request.session.get('user', '')
    new_search_phone = request.GET.get("phone", "")
    guests = Guest.objects.filter(phone__contains=new_search_phone)

    if len(guests) == 0:
        return render(request, "guest_manage.html", {"user": username,
                                                     "hint": "根据输入的手机号，查询结果为空！"})
    pageinator = Paginator(guests, 5)
    page = request.GET.get('page')
    try:
        contacts = pageinator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = pageinator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面
        contacts = pageinator.page(pageinator.num_pages)
    return render(request, 'guest_manage.html', {"user": username,
                                                 "guests": contacts,
                                                 "phone": new_search_phone})


# 签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {'event': event})


# 签到动作
@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone', '')
    print(phone)

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'phone error.'})

    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'event id or phone error.'})

    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': "sign in success!",
                                                   'guest': result})


# 退出登录
@login_required
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/index/')
    return response
