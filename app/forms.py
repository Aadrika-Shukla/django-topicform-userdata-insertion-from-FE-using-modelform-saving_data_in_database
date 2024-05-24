from django import forms

from app.models import *


'''#inorder to create model form we will inherit modelform class from forms
where we will create nested classes where first class is responsible just for defining a 
form as model form and 2nd class is responsible for declaring all the fields ,data of our model we choose
class meta --->M should always be capital


Using model form we can just create input fields or model forms are just for performing creation/insertion operation but not 
other crud operations that we can do in djnagoform ,as well as normal html forms

Using MODEL FORM we don't need to define every columns our model form do take care of that 

hence results in decrease in code redundancy,code mismatching of field name

if their is parent child relationship our modelfrom by default creates a dropdown for foreign key column data

'''

class Topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class Webpageform(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'


class Accessform(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
