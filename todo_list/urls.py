from django.urls import path
from . import views
urlpatterns = [
    #Today's list
    path('',views.home,name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('high/<list_id>', views.high, name="high"),
    path('prio', views.prio, name="prio"),
    path('medium/<list_id>', views.medium, name="medium"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('deleteAll', views.deleteAll, name="deleteAll"),
    path('deleteComplete', views.deleteComplete, name="deleteComplete"),
    #Today's Sub-List
    path('sub/<lists_id>',views.sub, name="sub"), 
    path('cross/<lists_id>', views.cross, name="cross"),
    path('ncross/<lists_id>', views.ncross, name="ncross"), 
    path('trash/<lists_id>', views.trash, name="trash"), 
    path('deleteAl', views.deleteAl, name="deleteAl"),
    path('deleteCompleted', views.deleteCompleted, name="deleteCompleted"),
    path('edits/<lists_id>', views.edits, name="edits"),
    #Tommorow's List
    path('tom/<listss_id>',views.tom, name="tom"), 
    path('cut/<listss_id>',views.cut, name="cut"), 
    path('dell/<listss_id>',views.dell, name="dell"), 
    path('dl/<listss_id>',views.dl, name="dl"), 
    path('top/<listss_id>',views.top, name="top"), 
    path('low/<listss_id>',views.low, name="low"), 
    path('clas',views.clas, name="clas"), 
    path('deleteeve',views.deleteeve, name="deleteeve"), 
    path('deleteComp',views.deleteComp, name="deleteComp"),
    path('change/<listss_id>',views.change, name="change"),
    #Tommorow's Sub-List
    path('subs/<list1_id>',views.subs, name="subs"),
    path('correct/<list1_id>',views.correct, name="correct"),
    path('quit/<list1_id>',views.quit, name="quit"),
    path('unquit/<list1_id>',views.unquit, name="unquit"),
    path('dust/<list1_id>',views.dust, name="dust"),
    path('deleteAd',views.deleteAd, name="deleteAd"),
    path('deleteDone',views.deleteDone, name="deleteDone"),
    
    
      

    
]
