from django.views.generic import TemplateView

from django.views.generic.edit import CreateView
#django에서 기본적으로 제공하는 폼
from django.contrib.auth.forms import UserCreationForm
# reverse는 패턴명을 인식하기 위해서 urls.py 모듈이 메모리에 로딩되어야함.
# 하지만 views.py 모듈이 로딩되고 처리되는 시점에서 urls.py 모듈이 로딩되지 않을 수 있음.
# 그래서 reverse_lazy를 쓴다함
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
