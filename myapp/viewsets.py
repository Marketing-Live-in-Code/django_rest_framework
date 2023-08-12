from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import Article, Classification
from .serializers import ArticleSerializer, ClassificationSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]
    
    # 挑選某文章類別
    @action(detail=True, methods=['get'])
    def pick_classify(self, request, pk=None):
        serializer = ArticleSerializer(
            Article.objects.filter(classification_id = pk), 
            many=True,context={'request': request})
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    permission_classes = [AllowAny]