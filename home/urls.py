from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # nested routing is what will be done here
    path('admission/', include([
        # Matches: /admission/
        path('', views.admission, name="admission"),
        # Matches: /admission/applying/
        path('applying/', views.applying, name="applying"),
    ])),
    path('stories', views.stories, name='stories'),
    path('gallery', views.gallery, name='gallery'),
    path('coming', views.coming, name='coming'),
    path('about', views.about_us, name='about'),
]
