from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookList(APIView):
    def get(self, request):

        books = Book.objects.all()

        price = request.query_params.get('price')
        title = request.query_params.get('title')

        price_lte = request.query_params.get('price_lte')
        price_gte = request.query_params.get('price_gte')


        if price:
            books = books.filter(price=price)
        if price_lte:
            books = books.filter(price__lte=price_lte)
        if price_gte:
            books = books.filter(price__gte=price_gte)
        if title:
            books = books.filter(title__icontains=title)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)