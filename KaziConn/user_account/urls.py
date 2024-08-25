from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListView, UserDetailView, UserCreateView, UserDeleteView, UserUpdateView, BlacklistTokenUpdateView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', BlacklistTokenUpdateView.as_view(), name='token_blacklist'),
    
    # User management
    path('api/users/', UserListView.as_view(), name='user_list'),
    path('api/users/create/', UserCreateView.as_view(), name='user_create'),
    path('api/users/<uuid:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('api/users/<uuid:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('api/users/<uuid:pk>/update/', UserUpdateView.as_view(), name='user_update'),
]
