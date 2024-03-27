from django.urls import path, include

urlpatterns = [
    # ... (existing URL patterns)
    path('contacts/', include('contacts.urls')),
]
