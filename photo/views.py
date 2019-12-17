from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.views import LoginRequiredMixin

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')

class AlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')

from django.shortcuts import redirect
from .forms import PhotoInlineFormSet

class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'description']
    template_name = 'photo/album_form.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
        #POST요청일 경우 formset 컨텍스트 변수를 POST, FILES를 이용해 지정. FILES는 파일 업로드가 이뤄지기때문.
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        #GET요청일 경우
        else:
            context['formset'] = PhotoInlineFormSet
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        # formset 객체 구하기
        formset = context['formset']

        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            #form의 데이터를 테이블에 저장. 앨범 레코드 하나 생성
            self.object = form.save()
            #폼셋의 메인 객체를 방금 테이블에 저장한 객체로 지정.
            formset.instance = self.object
            formset.save()
            # get_absolute_url() 호출, 앨범 상세페이지로 이동
            return redirect(self.object.get_absolute_url())
        else:
            #폼셋 데이터가 유효하지 않으면, 메인 폼, 인라인 폼셋 출력, 데이터는 다시보여줌
            return self.render_to_response(self.get_context_data(form=form))

class AlbumPhotoUV(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['name', 'description']
    template_name = 'photo/album_form.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
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
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
# Create your views here.


