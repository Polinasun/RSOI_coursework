from django.urls import path
# from .views.dancers_error_view import DancersErrorLogView, DancersErrorLogsView
from .views.log_view import LogsView, LogView
from .views.stat_view import ClubsStatView

urlpatterns = [
    path('logs/', LogsView.as_view()),
    path('log/<uuid:uuid>/', LogView.as_view()),
    path('stat/clubs/<uuid:uuid>/', ClubsStatView.as_view())
]