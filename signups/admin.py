from django.contrib import admin

# Register your models here.
from .models import SignUp, Subjects, Student, Book, Publisher, Author, UserProfile, User


class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

class SubjectsAdmin(admin.ModelAdmin):
    class Meta:
        model = Subjects

class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student



class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book

class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author

class PublisherAdmin(admin.ModelAdmin):
    class Meta:
        model = Publisher


class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Student, StudentAdmin)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)

admin.site.register(UserProfile, UserProfileAdmin)




