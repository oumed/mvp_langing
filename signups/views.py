from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, get_object_or_404, \
    redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, RedirectView, DetailView, ListView, FormView, CreateView, \
    UpdateView, DeleteView
from .forms import SignUpForm, ClientForm, NouveauContactForm, MultiSelecttForm, ContactForm, UserForm, UserProfileForm, \
    TodoForm
# Create your views here.
from django.contrib import messages
from .models import Subjects, Student,  Contact, Publisher, Book, Todo

from PIL import Image as PImage
from os.path import join as pjoin
from mvp_langing.settings import MEDIA_ROOT



from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms

@login_required()
def home(request):
    data =  {'first_name' : 'ABC',
            'last_name' : 'EFG',
            'email' : 'abc@yahoo.fr'}

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for joining.')
        return HttpResponseRedirect('/thank_you')
    return render_to_response('signup.html',
                              locals(),
                              context_instance=RequestContext(request))


def thank_you(request):
    return render_to_response('thank_you.html',
                              locals(),
                              context_instance=RequestContext(request))


def about_as(request):
    return render_to_response('about_as.html',
                              locals(),
                              context_instance=RequestContext(request))


def test_forms(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for joining.')
        return HttpResponseRedirect('/thank_you')
    return render_to_response('test_forms.html',
                              locals(),
                              context_instance=RequestContext(request))


class StudentForm(ModelForm):
    subject = forms.ModelMultipleChoiceField(Subjects.objects.all(),widget=FilteredSelectMultiple("Subjects",False,attrs={'rows':'10'}))
    subjectabc = forms.ModelMultipleChoiceField(Subjects.objects.all(),widget=FilteredSelectMultiple("Subjects",False,attrs={'rows':'10'}))

    class Meta:
        model = Student


def Form(request):
    form=StudentForm()

    if request.POST:
        form = StudentForm(request.POST)
        form.save()
        return render_to_response("success.html")
    else:
        return render_to_response("form.html",{'form': form})


def bootstrap(request):
     return render_to_response('bootstrap.html',
                              locals(),
                              context_instance=RequestContext(request))


def angularjs(request):

    name = 'Test Django'
    return render_to_response('AngularJS.html',
                              locals(),
                              context_instance=RequestContext(request))

def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d



# class ProfileForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         exclude = ["posts", "user"]
#
# def profile(request, pk):
#     """Edit user profile."""
#     profile = UserProfile.objects.get(user=pk)
#     img = None
#
#     if request.method == "POST":
#         pf = ProfileForm(request.POST, request.FILES, instance=profile)
#         if pf.is_valid():
#             pf.save()
#             # resize and save image under same filename
#             imfn = pjoin(MEDIA_ROOT, profile.avatar.name)
#             im = PImage.open(imfn)
#             im.thumbnail((160,160), PImage.ANTIALIAS)
#             im.save(imfn, "JPEG")
#     else:
#         pf = ProfileForm(instance=profile)
#
#     if profile.avatar:
#         img = "/media/" + profile.avatar.name
#     return render_to_response("profile.html", add_csrf(request, pf=pf, img=img))




def nouveau_contact(request):
    sauvegarde = False

    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()
            sauvegarde = True
    else:
        form = NouveauContactForm()

    return render(request, 'contact.html',locals())


def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'voir_contacts.html',{'contacts':contacts})


def multiselect(request):

    if request.method == "POST":
        form = MultiSelecttForm(request.POST)
        if form.is_valid():
            print form.cleaned_data["authors"]
            print form.cleaned_data["nom"]
            print form.cleaned_data["adresse"]
    else:
        form = MultiSelecttForm()

    return render(request, 'multiselect.html',locals())




class MyView(View):

    def get(self, request, *args, **kwargs):
        print request
        print '*********************'
        print args
        print '*********************'
        print kwargs

        id = kwargs['id_test']
        request.user
        return HttpResponse('{0} , {1} : Hello, World!'.format(request.user ,id))



class HomePageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['id'] = kwargs['pk']
        context['latest_articles'] = Contact.objects.all()[:5]
        return context


class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, pk):
        article = get_object_or_404(Contact, pk=pk)
        article.save()
        return reverse('homepageview', args=(pk,))

class ArticleDetailView(DetailView):

    model = Contact
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        print kwargs
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['contact'] = kwargs
        return context


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favourite_publishers'


class PublisherDetail1(DetailView):
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()


class PublisherDetail(DetailView):
    model = Publisher
    queryset = Publisher.objects.all()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.filter()
        pub = self.object
        context['book_list'] = pub.book_set.all()
        return context

class BookList(ListView):
    # queryset = Book.objects.order_by('-publication_date')
    queryset = Book.objects.filter(pk__in=[2,3,4])
    context_object_name = 'book_list'

class PublisherBookList(ListView):
    template_name = 'signups/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context

class ContactView(FormView):
    template_name = 'signups/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)


class thanks(TemplateView):
    template_name = 'signups/thanks.html'


def authentification(request, username, password):
    user = authenticate(username= username, password=password)
    print user
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
            return HttpResponse("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
            return HttpResponse("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return HttpResponse("The username and password were incorrect.")


def create_permission(request):
    content_type = ContentType.objects.get_for_model(Book)
    permission = Permission.objects.create(codename='can_publish',name='Can Publish Book',content_type=content_type)
    user = User.objects.get(username='user1')

    if user:
        user.user_permissions.add(permission)

    return HttpResponse(user.username + "Can Publish Book")

def authenticate_login(request):

    username = request.user.username
    password = request.user.password
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("User Login")
        else:
            return HttpResponse("User No Active")

    else:
        return HttpResponse("User Invalid")


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

# Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login_user.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")



def user_permissions(request):
    # ... my view actions ...
    list_permissions = []
    user_permissions = request.user.user_permissions.all()
    for p in user_permissions:
        list_permissions.append(p.name)
        print p

    data = ''.join(list_permissions)
    return HttpResponse("List the permission for {0} : {1}".format(request.user.username,data))


@login_required
@user_passes_test(lambda u: u.groups.filter(name='search').count() == 0, login_url='/')
def some_view(request):
    # Do whatever this view should do
    return HttpResponse("OK test Success")


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
            return False
    return user_passes_test(in_groups)


@login_required
@group_required('admins','editors')
def some_view_group_required(request):
    # Do whatever this view should do
    return HttpResponse("OK test Success")

#*******************************************************

class TodoList(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'

class TodoDetail(DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    @method_decorator(permission_required('todo.view_todo'))
    def dispatch(self, *args, **kwargs):
        return super(TodoDetail, self).dispatch(*args, **kwargs)

class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/form.html'

    # @method_decorator(permission_required('todo.add_todo'))
    # def dispatch(self, *args, **kwargs):
    #     return super(TodoCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return redirect(self.object)

class TodoUpdate(UpdateView):
    template_name = 'todo/form.html'
    model = Todo
    form_class = TodoForm
    @method_decorator(permission_required('signups.change_todo'))
    def dispatch(self, *args, **kwargs):
        return super(TodoUpdate, self).dispatch(*args, **kwargs)

class TodoDelete(DeleteView):
    template_name = 'todo/delete.html'
    model = Todo
    @method_decorator(permission_required('todo.delete_todo'))
    def dispatch(self, *args, **kwargs):
        return super(TodoDelete, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        # To do this because the success_url class variable isn't reversed...
        return reverse('todo_list')


class TestBase(TemplateView):
    # super(TestBase,self).__init__(self,**kwargms)
    '''
    '''
    template_name = 'todo/test.html'
