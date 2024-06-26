from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.home,name='index'),
    path('contact',views.contact,name='contact'),
    path('apply',views.apply,name='apply'),
    path('company-registration',views.company_registration,name='company-registration'),
    path('student-registration',views.student_registration,name='student-registration'),
    path('signin',views.login,name='signin'),
    path('adminn',views.adminn,name='adminn'),
    path('view-feedback',views.view_feedback,name='view-feedback'),
    path('view-students',views.view_student,name='view-students'),
    path('view-companies',views.view_company,name='view-companies'),
    path('delete-company',views.delete_company,name='delete-company'),
    path('delete-student',views.delete_student,name='delete-student'),
    path('add-students',views.add_student,name='add-students'),
    path('add-companies',views.add_company,name='add-companies'),
    path('logout',views.logout,name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)