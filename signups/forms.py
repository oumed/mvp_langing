from django import forms
from django.contrib.auth.models import User
from .models import SignUp, Client, Author, UserProfile, Todo


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp


class ClientForm(forms.ModelForm):
    address = forms.ModelMultipleChoiceField(queryset=Client.objects.all())
    class Meta:
        model = Client

# class Contact(models.Model):
#     nom = models.CharField(max_length=255)
#     adresse = models.TextField()
#     photo = models.ImageField(upload_to="photos/")
#
#     def __unicode__(self):
#            return self.nom


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()


class MultiSelecttForm(forms.Form):

    choice_Field = [
        (1, 'Profile Set'),
        (2, 'Ip Address'),
        (3, 'Ip Address'),
    ]

    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.none(), label='Author', required=False)
    choiceField   = forms.ChoiceField(label='Profile set / IP Address', choices=choice_Field, widget=forms.RadioSelect)
    def __init__(self, *args, **kwargs):
        super(MultiSelecttForm, self).__init__(*args, **kwargs)
        #self.fields['authors'].widget.attrs['class'] = 'multiselect'
        #self.fields['authors'].widget.attrs['multiple'] = 'multiple'
        self.fields['authors'].queryset = Author.objects.all()


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'priority', 'due_on',)