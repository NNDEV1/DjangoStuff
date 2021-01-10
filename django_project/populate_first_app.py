import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_project.settings')

import django
django.setup()

import random
from my_first_app.models import Webpage, Topic, AcessRecord
from faker import Faker

fakegen = Faker()
topics = ['social', 'news', 'politics', 'games', 'market',]

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for topic in range(N):

        top = add_topic()

        fakeurl = fakegen.url()
        fakedate = fakegen.date()
        fakename = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic=top, url = fakeurl, name=fakename)[0]
        acc_rec = AcessRecord.objects.get_or_create(name=webpage, date = fakedate)

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('script populated')
