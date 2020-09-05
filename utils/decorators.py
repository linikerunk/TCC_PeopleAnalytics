from functools import wraps

from django.shortcuts import redirect


def first_register(redirect_to='users:first_register'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.id == None:
                pass
            elif request.user.employee is None:
                return redirect(redirect_to)
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator