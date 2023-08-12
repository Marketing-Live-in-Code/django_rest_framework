from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Article, Classification
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def test(request):
    return render(request, 'test.html', {
        'title': '測試',
        'data' : '這裡是標題'
    })

#---------- 自訂API ----------
class chapter(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        Classification_data = Classification.objects.all()
        data = {}
        for cls in Classification_data:
            Article_data = Article.objects.filter(classification_id = cls.id)
            temp_array = []
            for atc in Article_data:
                temp_array.append(atc.title)
            data[cls.id] =temp_array
        return Response(data, status=status.HTTP_200_OK)