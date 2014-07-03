from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.sites.models import Site
# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)



class Client(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)


class Subjects(models.Model):
    sub_name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)


class Student(models.Model):
    name=models.CharField(max_length=100)
    subject=models.ManyToManyField(Subjects)


###############################


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline


# class UserProfile(models.Model):
#     avatar = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
#     posts = models.IntegerField(default=0)
#     user = models.ForeignKey(User, unique=True)
#
#     def __unicode__(self):
#         return unicode(self.user)


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __unicode__(self):
        return self.nom


# models.py
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    class Meta:
        permissions = (
            ("can_add_users", "Can add new users"),
            ("can_edit_users", "Can change other users"),
            ("can_activate_users", "Can activate other users"),
            ("can_deactivate_users", "Can deactivate other users"),
        )


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



class Todo(models.Model):
    PRIORITY_LIST = (
        (0, 'Low'),
        (5, 'Normal'),
        (10, 'High'),
        (15, 'Urgent'),
    )
    title = models.CharField(max_length=40)
    owner = models.ForeignKey(User)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_LIST, default=5)
    added_on = models.DateTimeField(auto_now_add=True)
    due_on = models.DateField()
    class Meta:
        permissions = (('view_todo', 'Can view todo'),)
        ordering = ['due_on']
    def __unicode__(self):
        return u"%s" % self.title


    @models.permalink
    def get_absolute_url(self):
        return ('todo_detail', [int(self.pk)])