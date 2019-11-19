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
#create view here!!!
class PasteCreate(CreateView):
    model = Paste
    fields = ['Age','Strain','Genotype','Contact','name']
    success_url = reverse_lazy('pastebin_paste_list')

class PasteList(ListView):
    model = Paste
    template_name = "pastebin/paste_list.html"
    queryset = Paste.objects.all()
    context_object_name = 'queryset'

class PasteDetail(DetailView):
    model = Paste
    template_name = "pastebin/paste_detail.html"

class PasteDelete(DeleteView):
    model = Paste
    success_url = reverse_lazy('pastebin_paste_list')

class PasteUpdate(UpdateView):
    model = Paste
    fields = ['Age','Strain','Genotype','Contact','name']
    success_url = reverse_lazy('pastebin_paste_list')

class SearchResultsView(ListView):
    model = Paste
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paste.objects.filter(
            Q(Age__gte=query)
        )
        return object_list

class SearchResultView(ListView):
    model = Paste
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paste.objects.filter(
            Q(Age__lte=query)
        )
        return object_list

class ResultsdropView(ListView):
    model = Paste
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paste.objects.filter(
            Q(Strain__exact=query)
        )
        return object_list

class Tableview(ListView):
    model = Paste
    template_name = "pastebin/search_results.html"
    queryset = Paste.objects.all()
    context_object_name = 'queryset'

class searchview(ListView):
    model = Paste
    template_name = "pastebin/search_results.html"
    def search(request):
        user_list = Paste.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        return render(request, "pastebin/search_results.html", {'filter': user_filter})
