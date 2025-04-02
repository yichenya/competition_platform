from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserDetailView
from django.contrib import admin
from django.http import HttpResponse

# 定义一个简单的根路径视图
def home(request):
    return HttpResponse("Welcome to the User Service!")


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserDetailView.as_view(), name='user_detail'),
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 添加根路径
]