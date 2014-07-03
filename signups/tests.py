class EvenExtractor(object):
    def __init__(self, alist):
        self.l = alist

    def extract(self):
        return [i for i in self.l if i%2 == 0]


class OddExtractor(EvenExtractor):
    def extract(self):
        return [i for i in self.l if i%3 != 0]

    def message(self):
        print "Balabla"


class Thought(object):
    def __init__(self):
        pass
    def message(self):
        print "I feel like I am diagonally parked in a parallel universe."

class Advice(Thought):
    def __init__(self):
        super(Advice, self).__init__()

    def message(self):
        super(Advice, self).message()
        print "Warning: Dates in calendar are closer than they appear"




class test(OddExtractor,Advice):
    """
    test
    """

from django.views.generic.list import ListView
from signups.models import Author

class ArticleListView(ListView):
    model = Author




class toto(EvenExtractor):
    """
    tst
    """

class client():
    def __init__(self, a,b,c):
        self.nom = a
        self.prenom = b
        self.address = c
        # self.rep = 'Rep_ndndndn'

    def des(self):
        return  self.nom +" "+ self.prenom + " " +self.address


class custom():
    def __init__(self, e):
        self.rep = e

    def desc(self):
        return  self.rep


class test1(client,custom):
    """
        test1
    """
class test2(custom, client):
    """
        test2
    """






