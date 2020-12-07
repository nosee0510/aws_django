from django.views.generic import TemplateView

from django.views.generic import CreateView     #새로운 레코드 생성하기위한 폼을 보여주고 입력된 데이터로 레코드를 생성해주는 뷰
from django.contrib.auth.forms import UserCreationForm #user 모델의 객체를 생성하기 위해 보여주는 폼
from django.urls import reverse_lazy #url 패턴을 반환하는 함수이다 revese() lazy 둘다 허나 lazy는 urls.py가 로딩이안될수도있으므로 그떄 사용하도록 즉, 늦게 실행해라 url 담으로
from django.contrib.auth.mixins import AccessMixin #다중상속을 위한 매커니즘:Mixin 뷰처리 단게로 집입단계에서 적절한권한이 있는지 판별할떄 사용하는 믹스인 클래스

#--- Templateview


class HomeView(TemplateView): #db와 상관없이 html 문서만 연결해주는것이 templateview
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm  #model = user 가없는이유는 이 UserCreationForm 안에 지정돼있기 떄문이다.
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"


def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
