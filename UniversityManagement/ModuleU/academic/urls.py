from django.urls import path
from ModuleU.academic.views import formContact, contact, register_request, login_request, logout_request, home
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView, CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView, CarrerListCreateAPIView, CarrerRetrieveUpdateDestroyAPIView, EnrollmentListCreateAPIView, EnrollmentRetrieveUpdateDestroyAPIView
from .views import CourseCreateView, StudentCreateView, CareerCreateView, EnrollmentCreateView
from rest_framework_simplejwt import views as jwt_views

app_name = "academic"

urlpatterns = [
    path('home/', home, name='home'),
    path('formContact/', formContact, name='formContact'),
    path('contact/', contact, name='contact'),
    path('student/', StudentCreateView.as_view(), name='student-create'),
    path('course/', CourseCreateView.as_view(), name='course-create'),
    path('career/', CareerCreateView.as_view(), name='career-create'),
    path('enrollment/', EnrollmentCreateView.as_view(), name='enrollment-create'),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path("logout/", logout_request, name= "logout"),

    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('api/v1/students/<pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-retrieve-update-destroy'),
    path('api/v1/courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('api/v1/courses/<pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-retrieve-update-destroy'),
    path('api/v1/career/', CarrerListCreateAPIView.as_view(), name='career-list-create'),
    path('api/v1/career/<pk>/', CarrerRetrieveUpdateDestroyAPIView.as_view(), name='carrer-retrieve-update-destroy'),
    path('api/v1/enrollment/', EnrollmentListCreateAPIView.as_view(), name='enrollment-list-create'),
    path('api/v1/enrollment/<pk>/', EnrollmentRetrieveUpdateDestroyAPIView.as_view(), name='enrollment-retrieve-update-destroy')
]