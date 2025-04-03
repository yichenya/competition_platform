from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Registration, School,Competition
from .serializers import RegistrationSerializer, SchoolSerializer , CompetitionSerializer

# 自定义分页类
class RegistrationPagination(PageNumberPagination):
    page_size = 10  # 每页显示 10 条数据
    page_size_query_param = 'page_size'
    max_page_size = 100



# 学校列表视图
class SchoolListView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]


# 报名视图
class RegistrationListCreateView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    pagination_class = RegistrationPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class RegistrationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CompetitionView(generics.RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        # 假设只有一个比赛，直接返回第一个
        return Competition.objects.first()
    
