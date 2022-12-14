from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.createListing, name="createListing"),
    path("productView/<int:id>",views.productView, name="productView"),
    path("editListing/<int:id>",views.editListing, name="editListing"),
    path("watchlistSwitch/<int:id>/<int:switch>", views.watchlistSwitch, name="watchlistSwitch"),
    path("watchlistView", views.watchlistView, name="watchlistView"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("addBid/<int:id>", views.addBids, name="addBids"),
    path("close/<int:id>", views.close, name="close"),
]
