from django.db import models
from django.utils import timezone
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Post(models.Model):
# Native fields  
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    verse_title = models.CharField(max_length=100)
    verse = models.TextField()
    commentary_title = models.CharField(max_length=200)
    commentary = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
# Relationships to other models
    source_authors = models.ManyToManyField('Writer', null=True)
    source_translators = models.ManyToManyField('Translator', null=True)
    source = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 
        
class Writer(models.Model):
    """
    Model representing an author.
    """
    writer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField(null=True, blank=True)
    year_of_death = models.IntegerField(null=True, blank=True)
    profile = models.TextField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('writer-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
        
class Translator(models.Model):
    """
    Model representing a translator.
    """
    translator_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField(null=True, blank=True)
    year_of_death = models.IntegerField(null=True, blank=True)
    profile = models.TextField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('translator-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
        
class Book(models.Model):
    """
    Model representing a book.
    """
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Writer', on_delete=models.SET_NULL, null=True)
    first_edition = models.IntegerField(null=True, blank=True)
    translator_note = models.CharField(max_length=200, null=True, blank=True)
    translators = models.ManyToManyField('Translator')
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    book_url = models.URLField(null=True, blank=True)
        
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])
        
#class Card(models.Model):
    """
    Model representing a Bootstrap Card
    """
    #image_url = models.URLField(null=True, blank=True)
    #title = models.CharField(max_length=200)
    #text = models.TextField(max_length=1000)
    #list_item = models.ManyToManyField('ClassListItem')
    
    #def __str__(self):
    """
    String for representing the Model object.
    """
        #return self.title
        
#class ClassListItem(models.Model):
    """
    Model representing List Items for the Card class
    """
    #item_text = models.CharField()
    
    #def __str__(self):
    """
    String for representing the Model object.
    """
        #return self.title
    