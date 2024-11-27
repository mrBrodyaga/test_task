import pandas as pd

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from materials.models import (
    Material,
    Сategory,
)
from .serializers import (
    MaterialSerializer,
    СategorySerializer,
    CategoryTreeSerializer,
)


class MaterialViewSet(viewsets.ModelViewSet):
    """Отображение материалов"""

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


    @action(detail=False, methods=['POST'])
    def upload_excel(self, request):
        if 'file' not in request.FILES:
            return Response({'error': 'Файл не загружен'}, status=status.HTTP_400_BAD_REQUEST)
        
        excel_file = request.FILES['file']
        
        try:
            df = pd.read_excel(excel_file)
            for _, row in df.iterrows():
                Material.objects.create(
                    name=row['name'],
                    code_material=row['code_material'],
                    price=row['price'],
                    category_id=row['category_id']
                )
            return Response({'message': 'Данные импортированы'}, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({'error': str(Exception)}, status=status.HTTP_400_BAD_REQUEST)


class СategoryViewSet(viewsets.ModelViewSet):
    """Отображение категорий"""

    queryset = Сategory.objects.all()
    serializer_class = СategorySerializer

    @action(detail=False, methods=['GET'])
    def tree(self, request):
        root_categories = Сategory.objects.filter(parent_category=None)
        serializer = CategoryTreeSerializer(root_categories, many=True)
        return Response(serializer.data)
