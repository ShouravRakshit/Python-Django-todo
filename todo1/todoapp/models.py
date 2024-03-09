from django.db import models
from django.forms import  ModelForm, Textarea

class Todo(models.Model):
    text = models.CharField(max_length =200)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.text

class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields =['text',]