from django.urls import path, include

from rest_framework import routers

from Pereval.views import PerevalCreateViewset, PerevalUpdateViewset, PerevalListView, PerevalUserListViewset

create_pereval = routers.DefaultRouter()
create_pereval.register(r'pereval_create', PerevalCreateViewset, basename='pereval_create')

edit_pereval = routers.DefaultRouter()
edit_pereval.register(r'pereval_update', PerevalUpdateViewset, basename='pereval_update')

urlpatterns = [
    path('perevals/', PerevalListView.as_view(), name='pereval_list'),
    path('perevals/create/', include(create_pereval.urls)),
    path('perevals/edit/', include(edit_pereval.urls)),
    path('perevals/user__email=<str:email>', PerevalUserListViewset.as_view()),
]