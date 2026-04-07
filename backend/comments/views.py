from rest_framework import viewsets

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    # Additional settings.
