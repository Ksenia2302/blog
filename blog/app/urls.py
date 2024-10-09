from django.urls import path
from .views import index, view, contacts, reg, auth, logout

urlpatterns = [
    path('', index),
    path('view/<int:id>', view),
    path('contacts', contacts),
    path('reg', reg),
    path('auth', auth),
    path('logout', logout)
]

