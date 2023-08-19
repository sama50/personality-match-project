from django.contrib import admin
from app.models import Question , Options , MyUser , QueationAnswer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','title')

@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('id','question','option')

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id','email','name','crush','count','myid')

@admin.register(QueationAnswer)
class QueationAnswerAdmin(admin.ModelAdmin):
    list_display = ('id','user','name','ans')