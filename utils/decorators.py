from functools import wraps

from django.shortcuts import redirect


class FirstRegisterMixin:
    model = None
    template = None
    redirect_to = 'users:first_register'

    def get(self, request):
        print("I'm Here...")
        if self.request.user.id == None:
            pass
        elif self.request.user is not None:
            return redirect(redirect_to)
        return(request, self.template, {})




def first_register(redirect_to='users:first_register'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.id == None:
                pass
            elif request.user is not None:
                return redirect(redirect_to)
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator