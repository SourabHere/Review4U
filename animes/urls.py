from django.urls import path
from . import views
from rateeverything.views import index
urlpatterns = [
    path("",views.index,name="AnimeHome"),
    path("contact/",views.Contact,name="AnimeContact"),
    path("addrev/",views.addrev,name="AnimeAddrev"),
    path("myrev/<int:anime_id>",views.myreview,name="Animemyrev"),
    path("moredetail/<int:anime_id>",views.moredetail,name="Detail"),
    path("about/",views.about,name="Animeabout"),
    path("rateeverything/",index,name="Home")
]
