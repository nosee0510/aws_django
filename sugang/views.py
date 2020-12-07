from django.views.generic import ListView, DetailView
from sugang.models import Subject, Apply
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from sugang.forms import SubjectInlineFormSet

class SubjectLV(ListView):
    model = Subject


class SubjectDV(DetailView):
    model = Subject


class ApplyDV(DetailView):
    model = Apply


class ApplyCV(LoginRequiredMixin, CreateView):
    model = Apply
    fields = ('subject', 'name', 'number', 'major')
    success_url = reverse_lazy('sugang:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApplyChangeLV(LoginRequiredMixin, ListView):
    model = Apply
    template_name = 'sugang/apply_change_list.html'

    def get_queryset(self):
        return Apply.objects.filter(owner=self.request.user)


class ApplyUV(OwnerOnlyMixin, UpdateView):
    model = Apply
    fields = ('subject', 'name', 'number', 'major')
    success_url = reverse_lazy('sugang:index')


class ApplyDelV(OwnerOnlyMixin, DeleteView):
    model = Apply
    success_url = reverse_lazy('sugang:index')

#이하추가
# #---Change-list/Delete for Album


class SubjectChangeLV(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'sugang/subject_change_list.html'

    def get_queryset(self):
        return Subject.objects.filter(owner=self.request.user)


class SubjectDelV(OwnerOnlyMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('sugang:index')


#---(InlineFormSet) Create/Update for Album


class SubjectApplyCV(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('name', 'description')   #어떤 컬럼을 폼에 채울지.
    success_url = reverse_lazy('sugang:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SubjectInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = SubjectInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for applyform in formset:
            applyform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()   #앨범 레코드 생성.
            formset.instance = self.object #포토의 앨범컬럼에 앪범레코드의 id값을 설정
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SubjectApplyUV(OwnerOnlyMixin, UpdateView):
    model = Subject
    fields = ('name', 'description')
    success_url = reverse_lazy('sugang:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SubjectInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = SubjectInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))