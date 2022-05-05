from django.http import JsonResponse
from user.models import User
from utils.token import create_token
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            if user.password == password:
                token = create_token(username)
                return JsonResponse({
                    'errno': 0,
                    'msg': "登录成功",
                    'data': {
                        'username': user.username,
                        'authorization': token
                    }
                })
            else:
                return JsonResponse({'errno': 100003, 'msg': "密码错误"})
        else:
            return JsonResponse({'errno': 100004, 'msg': "用户不存在"})
    else:
        return JsonResponse({'errno': 200001, 'msg': "请求方式错误"})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        users = User.objects.filter(username=username)
        if users.exists():
            return JsonResponse({'errno': 300001, 'msg': "用户名已注册"})
        if password_1 != password_2:
            return JsonResponse({'errno': 300002, 'msg': "两次输入的密码不一致"})

        User.objects.create(username=username, password=password_1)
        return JsonResponse({'errno': 0, 'msg': "成功"})
    else:
        return JsonResponse({'errno': 200001, 'msg': "请求方式错误"})
