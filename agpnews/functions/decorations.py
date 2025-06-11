from django.http import Http404
from users.models import User

def allow_access_to(user_type_list):
    def decorator(func):
        def inner(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                raise Http404
            if user.profile.user_type in user_type_list:
                return func(request, *args, **kwargs)
            else:
                raise Http404
        return inner
    return decorator