from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Paste
from django.db.models import Q
from django.shortcuts import render
from .filters import UserFilter
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from accounts.models import Activation
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#create view here!!!
class PasteCreate(LoginRequiredMixin, CreateView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    fields = ['Age','Strain','Genotype','Contact','name']
    success_url = reverse_lazy('pastebin_paste_list')

class PasteList(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    template_name = "pastebin/paste_list.html"
    queryset = Paste.objects.all()
    context_object_name = 'queryset'

class PasteDetail(LoginRequiredMixin, DetailView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    template_name = "pastebin/paste_detail.html"

class PasteDelete(LoginRequiredMixin, DeleteView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    success_url = reverse_lazy('pastebin_paste_list')

class PasteUpdate(LoginRequiredMixin, UpdateView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    fields = ['Age','Strain','Genotype','Contact','name']
    if (Paste.Contact == Activation.user):
        success_url = reverse_lazy('pastebin_paste_list')

class SearchResultsView(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paste.objects.filter(
            Q(Age__gte=query)
        )
        return object_list

class SearchResultView(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paste.objects.filter(
            Q(Age__lte=query)
        )
        return object_list

class ResultsdropView(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paste.objects.filter(
            Q(Strain__exact=query)
        )
        return object_list

class Tableview(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    template_name = "pastebin/search_results.html"
    queryset = Paste.objects.all()
    context_object_name = 'queryset'

class searchview(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'redirect_to'
    model = Paste
    template_name = "pastebin/search_results.html"
    def search(request):
        user_list = Paste.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        return render(request, "pastebin/search_results.html", {'filter': user_filter})
