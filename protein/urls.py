from django.urls import path

from . import views

app_name = 'protein'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # # ex: /polls/5/
    path('shakes/<shake_name>/', views.shake, name='shake'),
    # # ex: /polls/5/results/
    path('shakes/', views.shakes, name='shakes'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf goes here ...

urlpatterns += staticfiles_urlpatterns()