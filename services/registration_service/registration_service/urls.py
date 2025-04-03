from django.urls import path
from .views import SchoolListView, RegistrationListCreateView, RegistrationDetailView ,CompetitionView

urlpatterns = [
    path('schools/', SchoolListView.as_view(), name='school-list'),  # 学校列表
    path('registrations/', RegistrationListCreateView.as_view(), name='registration-list-create'),  # 报名列表和创建
    path('registrations/<int:pk>/', RegistrationDetailView.as_view(), name='registration-detail'),  # 报名详情
    path('competition/', CompetitionView.as_view(), name='competition'),  # 获取比赛信息

    
]