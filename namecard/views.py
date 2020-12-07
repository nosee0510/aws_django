from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from namecard.models import Namecard_TBL
from namecard.forms import NamecardSearchForm
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.

class NamecardLV(ListView):
    model = Namecard_TBL
    context_object_name = 'namecards'

class NamecardDV(DetailView):
    model = Namecard_TBL
    context_object_name = 'namecards'

class SearchFormView(FormView):  #사용자가 입력한 값을 포스트/겟방식으로 처리해서 액션
    form_class = NamecardSearchForm
    template_name = 'namecard/namecard_tbl_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        namecard_list = Namecard_TBL.objects.filter(Q(name__icontains=searchWord) |
                                            Q(company__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = namecard_list

        return render(self.request, self.template_name, context)


class NamecardCreateView(LoginRequiredMixin, CreateView):
    model = Namecard_TBL
    template_name = 'namecard/namecard_form.html'
    fields = ['name', 'tel', 'company', 'email', 'group', 'birth_dt']
    success_url = reverse_lazy('namecard:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NamecardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'namecard/namecard_change_list.html'

    def get_queryset(self):
        return Namecard_TBL.objects.filter(owner=self.request.user)


class NamecardUpdateView(OwnerOnlyMixin, UpdateView):
    template_name = 'namecard/namecard_form.html'
    model = Namecard_TBL
    fields = ['name', 'tel', 'company', 'email', 'group', 'birth_dt']
    success_url = reverse_lazy('namecard:index')


class NamecardDeleteView(OwnerOnlyMixin, DeleteView):
    template_name = 'namecard/namecard_confirm_delete.html'
    model = Namecard_TBL
    success_url = reverse_lazy('namecard:index')