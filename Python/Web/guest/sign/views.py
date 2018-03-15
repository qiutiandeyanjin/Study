from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, "index.html")


# 登录动作
def login_action(request):
    if request.method == "POST":
        login_username = request.POST.get("username", "")
        login_password = request.POST.get("password", "")
        if login_username == '' or login_password == '':
            return render(request, "index.html", {"error": "username or password null"})

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


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    pageinator = Paginator(guest_list, 2)
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


# 嘉宾搜索
@login_required
def search_phone(request):
    username = request.session.get('user', '')
    new_search_phone = request.GET.get("phone", "")
    search_name_bytes = new_search_phone.encode(encoding="utf-8")
    guests = Guest.objects.filter(phone__contains=search_name_bytes)

    if len(guests) == 0:
        return render(request, "guest_manage.html", {"user": username,
                                                     "hint": "根据输入的手机号，查询结果为空！"})
    pageinator = Paginator(guests, 10)
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
    guest_list = Guest.objects.filter(event_id=eid)           # 签到人数
    sign_list = Guest.objects.filter(sign="1", event_id=eid)   # 已签到数
    guest_data = str(len(guest_list))
    sign_data = str(len(sign_list))
    return render(request, 'sign_index.html', {'event': event,
                                               'guest': guest_data,
                                               'sign': sign_data})


# 前端签到页面
def sign_index2(request, eid):
    event_name = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index2.html', {'eventId': eid,
                                                'eventNanme': event_name})


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
