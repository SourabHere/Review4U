from django.urls import path
from . import views
from rateeverything.views import index
urlpatterns = [
    path("",views.index,name="GamesHome"),
    path("addrev/",views.addrev,name="GamesAddrev"),
    path("contact/",views.contact,name="GamesContact"),
    path("about/",views.about,name="GamesAbout"),
    path("myrev/<int:games_id>",views.myreview,name="Myreview"),
    path("moredetail/<int:games_id>",views.detail,name="Detail"),
    path("rateeverything/",index,name="Home")
]
