#To use django forms 

from django import forms    
from .models import List
from .models import Lists
from .models import Tom
from .models import List1

class Listform(forms.ModelForm):        #Today's List
    class Meta:
        model = List
        fields= ["item", "completed","priority"]

class Listform1(forms.ModelForm):       #Today's Sub-List
    class Meta:
        model = Lists
        fields=["task", "done"]


class Listform2(forms.ModelForm):       #Tommorow's List
    class Meta:
        model = Tom
        fields= ["work", "exec","classify"]


class Listform3(forms.ModelForm):       #Tommorow's Sub-List
    class Meta:
        model = List1
        fields=["thing", "allright"]