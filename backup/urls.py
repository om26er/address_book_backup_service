from django.conf.urls import url

from backup import views

urlpatterns = [
    url(r'^api/add_contact$', views.AddContactView.as_view()),
]
