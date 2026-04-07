from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    # Additional settings.
