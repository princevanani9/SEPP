from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='election-home'),
    path('about/', views.about,name='election-about'),
    path('candidate/', views.candidate,name='election-candidate'),
    path('Vote/',views.vote,name="vote"),
    path('Voted/',views.voted,name="voted"),
    path('NotAllow/',views.notallow,name="notAllow"),
    path('Result/',views.result,name="result"),
    path('Present/',views.presentcandidate,name="present"),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
