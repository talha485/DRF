from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookList(APIView):
    def get(self, request):

        books = Book.objects.all()

        price = request.query_params.get('price')
        title = request.query_params.get('title')

        if price:
            books = books.filter(price__lte=price)

        if title:
            books = books.filter(title__icontains=title)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)