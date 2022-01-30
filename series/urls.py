from os import name
from django.urls import path,include
from . import views
from rateeverything.views import index
urlpatterns = [
    path("",views.index,name="SeriesHome"),
    path("contact/",views.contact,name="SeriesContact"),
    path("addrev/",views.addrev,name="SeriesReview"),
    path("aboutus/",views.about,name="SeriesAbout"),
    path("myreview/<int:series_id>",views.myreview,name="Myreview"),
    path("rateeverything/",index,name="Home"),
    path("moredetail/<int:series_id>",views.moredetail,name="MoreDetail")
]
