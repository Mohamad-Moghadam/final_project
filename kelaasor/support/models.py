from django.db import models

class Ticket(models.Model):
    TITLE= ['Sign-up issue', 'Log-in issue', 'Purchase issue', 'Other']
    title= models.Choices(*TITLE)
    content= models.TextField()
    user= models.CharField(max_length= 100)

class ResponseTicket(models.Model):
    question= models.ForeignKey(Ticket, on_delete= models.CASCADE, related_name= 'Response_of_each_ticket')
    content= models.TextField()