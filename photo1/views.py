from django.views.generic import ListView, DetailView
from photo1.models import Album1, Photo1

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from photo1.forms import PhotoInlineFormSet


class AlbumLV(ListView):
    model = Album1
    template_name = 'photo1/album1_list.html'


class AlbumDV(DetailView):
    model = Album1
    template_name = 'photo1/album1_detail.html'


class PhotoDV(DetailView):
    model = Photo1
    template_name = 'photo1/photo1_detail.html'

# 이하추가
# #---Create/Change-list/Update/Delete for Photo


class PhotoCV(LoginRequiredMixin, CreateView):
    model = Photo1
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo1:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo1
    template_name = 'photo1/photo1_change_list.html'

    def get_queryset(self):
        return Photo1.objects.filter(owner=self.request.user)


class PhotoUV(OwnerOnlyMixin, UpdateView):
    model = Photo1
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo1:index')


class PhotoDelV(OwnerOnlyMixin, DeleteView):
    model = Photo1
    success_url = reverse_lazy('photo1:index')

#이하추가
# #---Change-list/Delete for Album


class AlbumChangeLV(LoginRequiredMixin, ListView):
    model = Album1
    template_name = 'photo1/album1_change_list.html'

    def get_queryset(self):
        return Album1.objects.filter(owner=self.request.user)


class AlbumDelV(OwnerOnlyMixin, DeleteView):
    model = Album1
    success_url = reverse_lazy('photo1:index')


#---(InlineFormSet) Create/Update for Album


class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album1
    fields = ('name', 'description')   #어떤 컬럼을 폼에 채울지.
    success_url = reverse_lazy('photo1:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()   #앨범 레코드 생성.
            formset.instance = self.object #포토의 앨범컬럼에 앪범레코드의 id값을 설정
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumPhotoUV(OwnerOnlyMixin, UpdateView):
    model = Album1
    fields = ('name', 'description')
    success_url = reverse_lazy('photo1:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
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