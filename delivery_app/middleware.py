from django.contrib.auth import authenticate, login


class AuthenticationMiddleware:
    def __int__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = authenticate(request)
        if user is not None:
            login(request, user)
            request.user = user
        response = self.get_response(request)
        return response
