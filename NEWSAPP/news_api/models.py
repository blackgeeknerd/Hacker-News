from django.db import models



class NewsDB(models.Model):
    by = models.CharField(verbose_name="news posted by", max_length=255)
    username = models.CharField(max_length=1000)
    news_id = models.IntegerField()
    score = models.IntegerField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1000)
    text = models.TextField(null=True)
    url = models.URLField("URL", max_length=1000, null=True)
    type = models.CharField(max_length=1000)
    
    
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ['-time']
        
        
class Comment(models.Model):
    by = models.CharField(verbose_name="news posted by", max_length=255)
    username = models.CharField(max_length=1000)
    parent = models.ForeignKey(NewsDB, on_delete=models.CASCADE)
    text = text = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1000)
    


