from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    
    def my_options(self):
        return Options.objects.filter(question=self)
    
    def __str__(self):
        return self.title


class Options(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)


class MyUser(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    crush = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    myid = models.CharField(max_length=500)

class QueationAnswer(models.Model):
    user = models.ForeignKey(to=MyUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    
