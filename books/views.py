from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
# Create your views here.

# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True).data
        data = {
            "status": f"returned {len(books)} books",
            "books": serializer
        }
        return Response(data)

# class BookDeatilApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeatilApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id = pk)
        except:
            data = {
                "status": "book is not found"
            }
            return Response(data, status = status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book).data
        data = {
            "status": "Successfully",
            "book": serializer
        }
        return Response(data, status = status.HTTP_200_OK)

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status": "Book was created",
                "book": serializer.data
            }
            return Response(data)
        else:
            return Response({"status":"serializer is not valid"}, status = status.HTTP_400_BAD_REQUEST)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        # book = Book.objects.get(id = pk)
        book = get_object_or_404(Book, id=pk)
        data = request.data
        serializer = BookSerializer(instance = book, data = data,  partial = True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "Book was updated",
                "book": serializer.data
            }
            return Response(data)
        else:
            return Response({"status":"serializer is not valid"}, status = status.HTTP_400_BAD_REQUEST)

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id = pk)
        except:
            return Response({"status":"book is not found"}, status = status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({"status":"Book was deleted"})

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrievDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveALLApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookModelView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



@api_view(["GET"])
def list_api_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True).data
    context = {
        "data": serializer,
        "status":"Successfully"

    }
    return Response(context)



