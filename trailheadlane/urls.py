from django.conf.urls import patterns, url

urlpatterns = patterns("trailheadlane.views",

                       url(r"trailheadlane/$", "about", name="trailheadlane_about"),
                       url(r"^trailheadlane/trader/$", "trader", name="trailheadlane_trader"),
                       url(r"^trailheadlane/analyzer/$", "analyzer", name="trailheadlane_analyzer"),

                       )
