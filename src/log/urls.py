from django.urls import path
from . import views

urlpatterns = [
    path('log/create', views.logCreateView, name='log-create'),
    path('log/<uuid:pk>/detail',
         views.logDetailView, name='log-detail'),
    path('log/<uuid:pk>/update',
         views.LoggerUpdateView.as_view(), name='log-update'),
    path('log/', views.LoggerListView.as_view(), name='log-list'),
    path('log/uploadfile', views.fileUploadHandler, name='file-upload'),
    path('log/delete', views.logDeleteView, name='log-delete')
]
