from utils.token import check_token
from django.http import JsonResponse

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object


API_WHITELIST = ["/api/user/login", "/api/user/register"]


class AuthorizeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path not in API_WHITELIST:
            username = request.META.get('HTTP_USERNAME')
            token = request.META.get('HTTP_AUTHORIZATION')
            if username is None or token is None:
                return JsonResponse({'errno': 100001, 'msg': "未查询到登录信息"})
            else:
                if check_token(username, token):
                    pass
                else:
                    return JsonResponse({'errno': 100002, 'msg': "登录信息错误或已过期"})
        pass
