from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListApiView, list_api_view, BookDeatilApiView, BookCreateApiView,\
BookUpdateApiView, BookDeleteApiView, BookListCreateApiView, BookRetrieveUpdateApiView, \
BookRetrievDeleteApiView, BookRetrieveALLApiView, BookModelView

router = SimpleRouter()
router.register("books", BookModelView, basename="books")

urlpatterns = [
    # path("books/", BookListApiView.as_view()),
    # path("books/<int:pk>/", BookDeatilApiView.as_view()),
    # path("books/create/", BookCreateApiView.as_view()),
    path("books/<int:pk>/update/", BookUpdateApiView.as_view()),
    path("books/<int:pk>/delete/", BookDeleteApiView.as_view()),

    path("books/listcreate/", BookListCreateApiView.as_view()),
    # path("books/<int:pk>/listupdate/", BookRetrieveUpdateApiView.as_view()),
    # path("books/<int:pk>/listdelete/", BookRetrievDeleteApiView.as_view()),
    path("books/<int:pk>/listupdatedelete/", BookRetrieveALLApiView.as_view()),
    # path("books/", list_api_view),
]

urlpatterns += router.urls