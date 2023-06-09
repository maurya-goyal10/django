import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'first_project.settings')

import django
django.setup()

# FAKE DATA GENERATOR
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fake_gen = Faker()
topics = ['Search','Social','Sports','News','Marketplace']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # add topic name
        top = add_topic()

        # Create other fake data
        fake_url = fake_gen.url()
        fake_name = fake_gen.company()
        fake_date = fake_gen.date()

        wpg = Webpage.objects.get_or_create(topic = top,name = fake_name, url = fake_url)[0]
        wpg.save()

        acs_rec = AccessRecord.objects.get_or_create(name = wpg,date = fake_date)[0]
        acs_rec.save()

if __name__ == "__main__":
    print("Populating Script")
    populate(20)
    print("Completed Populating!!")
