from django.urls import path

from .views import ExamDetailView, ExamResultDetailView, ExamResultCreateView, ExamResultQuestionView, \
    ExamResultDeleteView
from .views import ExamListView
from .views import ExamResultCreateView
from .views import ExamResultQuestionView
from .views import ExamResultDetailView
from .views import ExamResultUpdateView


app_name = 'quizzes'

urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('<uuid:uuid>/', ExamDetailView.as_view(), name='details'),
    path('<uuid:uuid>/results/create/', ExamResultCreateView.as_view(), name='result_create'),
    path('<uuid:uuid>/results/<uuid:res_uuid>/questions/next/', ExamResultQuestionView.as_view(), name='question'),
    path('<uuid:uuid>/results/<uuid:res_uuid>/remove/', ExamResultDeleteView.as_view(), name='result_remove'),
    path('<uuid:uuid>/results/<uuid:res_uuid>/details/', ExamResultDetailView.as_view(), name='result_details'),
    path('<uuid:uuid>/results/<uuid:res_uuid>/update/', ExamResultUpdateView.as_view(), name='result_update'),


]
