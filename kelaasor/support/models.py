from django.db import models

class Ticket(models.Model):
    STATUS= [('pending', 'Pending'), ('resolved', 'Resolved'), ('rejected', 'Rejected'), ('closed', 'Closed')]
    TITLE= [('technical', 'Technical'), ('financial', 'Financial'), ('general', 'General')]
    title= models.CharField(max_length= 100, choices= TITLE)
    content= models.TextField()
    user= models.CharField(max_length= 100)
    status= models.CharField(max_length= 100, choices= STATUS, default= 'pending')

class ResponseTicket(models.Model):
    question= models.ForeignKey(Ticket, on_delete= models.CASCADE, related_name= 'Response_of_each_ticket')
    content= models.TextField()