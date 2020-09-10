from django.urls import path
from .views import TmpView, ContactView, excel, contact

urlpatterns = [
    # path('', TmpView.as_view()),
    path('', ContactView.as_view()),
    path('excel/', excel),
    path('email/', contact),
]