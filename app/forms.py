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
        fields='__all__'        # to create input fields for all the coloumns in out models
        #fields=['topic_name','name']           # to create specific input fields it will display column name in the order you pass
        #exclude=['email']                        # to create input field except the column name we specified
        #labels={'topic_name':'TOPIC NAME','name':'NAME'}       # by default label will be our coloumn name we declare in our models in ourder to give another lable name other than our coloumn name use lables in form of dictionary{'colomn name':'new label name'}
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea()}     # by default passowrd ,text area every field will be created as charfield only because we don't have any specific input type=password or textarea so we use here widgets to transform our charfield to password field or textarea
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea(attrs={'rows':3,'cols':3})}    # to customize text area block we give attrs attribute where values will be in form of dictionary



class Accessform(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'         # to create input fields for all the coloumns in out models
        #fields=['author','name']           # to create specific input fields it will display column name in the order you pass
        #exclude=['author']                        # to create input field except the column name we specified
        #labels={'date':'DATE','name':'NAME'}       # by default label will be our coloumn name we declare in our models in ourder to give another lable name other than our coloumn name use lables in form of dictionary{'colomn name':'new label name'}
        #widgets={'name':forms.Textarea()}     # by default passowrd ,text area every field will be created as charfield only because we don't have any specific input type=password or textarea so we use here widgets to transform our charfield to password field or textarea
        #widgets={'date':forms.PasswordInput,'name':forms.Textarea(attrs={'rows':3,'cols':3})}    # to customize text area block we give attrs attribute where values will be in form of dictionary

        