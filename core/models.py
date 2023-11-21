from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.CharField(max_length = 300, blank=False, null=False)
    
    def __str__(self):
        return self.id + ": " + self.quote
    
    
class Logo(models.Model):
    name = models.CharField(max_length = 150, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    url = models.URLField(max_length = 200, blank=True, null=True)
    # Image files
    png_file = models.ImageField(upload_to='media/png/', blank=False, null=False)
    jpg_file = models.ImageField(upload_to='media/jpg/', blank=False, null=False)
    svg_file = models.ImageField(upload_to='media/svg/', blank=False, null=False) 
    
    def __str__(self):
        return self.name
    

class LogoVariation(models.Model):
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE, related_name='variations')
    name = models.CharField(max_length = 150, blank=False, null=False)
    usage = models.TextField(blank=True, null=True)
    # Image files
    png_file = models.ImageField(upload_to='media/png/', blank=True)
    jpg_file = models.ImageField(upload_to='media/jpg/', blank=True)
    svg_file = models.ImageField(upload_to='media/svg/', blank=True)
    
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name
    
    