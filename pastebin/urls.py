from django.urls import path
from .views import PasteList, PasteDetail, PasteDelete, PasteUpdate, PasteCreate, SearchResultsView, SearchResultView, ResultsdropView, Tableview, searchview

urlpatterns = [
    path('pastex/', PasteCreate.as_view(), name='create'),
    path('', PasteList.as_view(), name='pastebin_paste_list'),
    path('paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
    path('paste/delete/<int:pk>', PasteDelete.as_view(), name='pastebin_paste_delete'),
    path('paste/edit/<int:pk>', PasteUpdate.as_view(), name='pastebin_paste_edit'),
    path('Search/', SearchResultsView.as_view(), name='searchg_results'),
    path('search/', SearchResultView.as_view(), name='searchl_results'),
    path('search_/', ResultsdropView.as_view(), name='search_results'),
    path('all/', Tableview.as_view(), name='table'),
    path('all/', searchview.as_view(), name='table'),
]
