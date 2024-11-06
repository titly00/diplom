from django.urls import path


from .views import ProjectViewSet, TaskViewSet, UserViewSet, TaskHistoryViewSet, ProfileViewSet, RegisterCreateAPIView
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects'),
router.register(r'tasks', TaskViewSet, basename='task'),
router.register(r'users', UserViewSet, basename='user'),
router.register(r'taskhistorys', TaskHistoryViewSet, basename='taskhistory'),
router.register(r'profiles', ProfileViewSet, basename='profile'),
# path('register/',  RegisterCreateAPIView.as_view(), name='employee_register'),










urlpatterns = [
path('api/token/', TokenObtainPairView.as_view(),
name='token_obtain_pair'),
path('register/',  RegisterCreateAPIView.as_view(), name='employee_register'),

path('api/token/refresh/', TokenRefreshView.as_view(),
name='token_refresh'),
]





urlpatterns += router.urls