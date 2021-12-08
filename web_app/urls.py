from django.urls import path
from . import views

urlpatterns = [
    path("", views.log_in, name="log_in"),
    path("signup", views.sign_up, name="sign_up"),
    path("<int:student_pk>/", views.main_page, name="main_page"),
    path("<int:student_pk>/invalid", views.invalid_input, name="invalid_input"),
    path("<int:student_pk>/account", views.edit_account, name="edit_account"),
    path("<int:student_pk>/account/update", views.update_account, name="update_account"),
    path("<int:student_pk>/history", views.student_record, name="student_record"),
    path("<int:student_pk>/add", views.add_record, name="add_record"),
    path("<int:student_pk>/remove", views.remove_record, name="remove_record"),
]
