from django.db import models

# Create your models here.
class Email(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email_from = models.EmailField(max_length=254)
    email_to = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return f'from: {self.email_from} | to: {self.email_to}, subject: {self.subject} created at: {self.created_at}'