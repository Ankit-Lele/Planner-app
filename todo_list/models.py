from django.db import models

class List(models.Model):                               #For Today's List 
    item = models.CharField(max_length=200)             #varaibles and their values/range
    completed = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '|' + str(self.completed) + '|' + str(self.priority)

        
class Lists(models.Model):                          #For Today's Sub-List 
    task = models.CharField(max_length=2000)        #varaibles and their values/range
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + '|' + str(self.done)


class Tom(models.Model):                            #For Tomorrows List
    work= models.CharField(max_length=200)          #varaibles and their values/range
    exec = models.BooleanField(default=False)
    classify = models.BooleanField(default=False)

    def __str__(self):
        return self.work + '|' + str(self.exec) + '|' + str(self.classify)


class List1(models.Model):                              #For Tomorrows Sub-List
    thing = models.CharField(max_length=2000)           #varaibles and their values/range
    allright = models.BooleanField(default=False)

    def __str__(self):
        return self.thing + '|' + str(self.allright)
