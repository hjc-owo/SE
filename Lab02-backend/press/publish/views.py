import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from publish.models import Author, Article  # 引入数据库 Author 对象


@csrf_exempt  # 跨域设置
def register(request):  # 继承请求类
    if request.method != 'POST':  # 判断请求方式是否为 POST（要求POST方式）
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    username = request.POST.get('username')  # 获取请求数据
    password_1 = request.POST.get('password_1')
    password_2 = request.POST.get('password_2')
    if re.match("^[A-Za-z0-9]+$", username) is None:
        return JsonResponse({'errno': 1003, 'msg': "用户名不合法"})
    elif password_1 != password_2:  # 若两次输入的密码不同，则返回错误码errno和描述信息msg
        return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
    elif Author.objects.filter(username=username).exists():
        return JsonResponse({'errno': 1004, 'msg': "用户名已存在"})
    elif re.match("^(?=.*\d)(?=.*[A-Za-z]).{8,18}$", password_1) is None:
        return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
    else:
        # 数据库存取：新建 Author 对象，赋值用户名和密码并保存
        new_author = Author(username=username, password=password_1)
        new_author.save()  # 一定要save才能保存到数据库中
        return JsonResponse({'errno': 0, 'msg': "注册成功"})


@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    username = request.POST.get('username')  # 获取请求数据
    password = request.POST.get('password')
    if not Author.objects.filter(username=username):
        return JsonResponse({'errno': 1006, 'msg': "哈哈！还没注册吧！"})
    author = Author.objects.get(username=username)
    if author.password == password:  # 判断请求的密码是否与数据库存储的密码相同
        request.session['username'] = username  # 密码正确则将用户名存储于session（django用于存储登录信息的数据库位置）
        return JsonResponse({'errno': 0, 'msg': "登录成功"})
    else:
        return JsonResponse({'errno': 1002, 'msg': "密码错误"})


@csrf_exempt
def logout(request):
    request.session.flush()
    return JsonResponse({'errno': 0, 'msg': "注销成功"})


@csrf_exempt
def release(request):
    username = request.POST.get('username')
    if not request.session.get('username') == username:
        return JsonResponse({'errno': 2001, 'msg': "是不是没登录？"})
    title = request.POST.get('title')
    description = request.POST.get('description')
    content = request.POST.get('content')
    if title == "":
        return JsonResponse({'errno': 2002, 'msg': "为什么不写文章标题？"})
    elif description == "":
        return JsonResponse({'errno': 2003, 'msg': "不稍微写一下描述性文字？"})
    elif content == "":
        return JsonResponse({'errno': 2004, 'msg': "不写文章内容？"})
    else:
        new_article = Article(
            title=title,
            description=description,
            content=content,
            author=Author.objects.get(username=username)
        )
        new_article.save()
        return JsonResponse({'errno': 0,
                             'msg': "发布时间是："
                                    + new_article.create_time.strftime("%Y-%m-%d, %H:%M:%S")
                                    + "。文章发布成功，内容正在审核，请不要着急捏。现在文章的状态是："
                                    + new_article.get_status_display() + "。"})


@csrf_exempt
def search_list(request):
    username = request.POST.get('username')
    if not request.session.get('username') == username:
        return JsonResponse({'errno': 2001, 'msg': "是不是没登录？"})

    want_article_status = request.POST.get('want_article_status')
    if re.match("^[0-2]$", want_article_status) is None:
        return JsonResponse({'errno': 3001, 'msg': "文章是不是没有这个状态？"})
    article_list = Article.objects.filter(status=want_article_status,
                                          author=Author.objects.get(username=username))
    if not article_list.exists():
        return JsonResponse({'errno': 3002, 'msg': "您目前没有这种状态的文章哦～"})
    want_article_status_data = []
    for article in article_list:
        want_article_status_item = {
            "title": article.title,
            "description": article.description,
            "create_time": article.create_time.strftime("%Y-%m-%d, %H:%M:%S")
        }
        want_article_status_data.append(want_article_status_item)
    return JsonResponse({'errno': 0, 'msg': "查询成功", 'data': want_article_status_data})
