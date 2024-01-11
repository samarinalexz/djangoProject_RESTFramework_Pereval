from django.urls import path, include

from rest_framework import routers

from Pereval.views import PerevalCreateViewset, PerevalUpdateViewset, PerevalListView, PerevalUserListViewset

create_pereval = routers.DefaultRouter()
create_pereval.register(r'', PerevalCreateViewset)

edit_pereval = routers.DefaultRouter()
edit_pereval.register(r'', PerevalUpdateViewset)

urlpatterns = [
    path('perevals/', PerevalListView.as_view()),
    path('perevals/create/', include(create_pereval.urls)),
    path('perevals/edit/', include(edit_pereval.urls)),
    path('perevals/user__email=<str:email>', PerevalUserListViewset.as_view()),
]