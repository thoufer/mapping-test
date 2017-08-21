from django.conf.urls import url
from .views import  ObservationCreateView, ObsAddView, LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name = 'index'),
    url(r'^add/$', ObservationCreateView.as_view(), name='create'),
    url(r'^add_crispy/$', ObsAddView.as_view(), name='create2'),
    #url(r'^edit/$', ObservationEditView.as_view(), name = 'edit'),
]
