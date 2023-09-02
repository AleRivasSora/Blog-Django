#from django.test import TestCase
import sys
sys.path.append('../../')

from blogProyecto.wsgi import *

from coreBlog.models import Type

query = Type.objects.all()

print(query)

#t = Type(names ='no residencial').save()

t = Type.objects.get(id=1)
print(t)


# Create your tests here.
