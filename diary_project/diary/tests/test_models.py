from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from diary.models import Entry, Tag

User = get_user_model()

class TagCaseTest(TestCase):
    """ We create one object for all tests """
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name="Training")

    """ Test for the uniqueness of the tag name """
    def test_case_unique(self):
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="Training")

    """ We check the __str__ class Tag method"""
    def test_case_str_method(self):
        self.assertEqual(str(self.tag.name), "Training")
    
    """ Check for the case of the uniqueness of the Tag name """
    def test_case_register_unique(self):
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="training")


class EntryCaseTest(TestCase):
    """ Creates a new object each time for each test """
    def setUp(self):
        self.author = User.objects.create_user(username="Vadim")

    """ A test case to validate the models.CASCADE method """
    def test_case_delete(self):
        Entry.objects.create(
            author=self.author,
            title="test header",
            content="Here is the content for Django tests"
            )
        self.author.delete()
        self.assertEqual(Entry.objects.count(), 0)

    """ We connect and check the tag, class ManyToManyField """
    def test_case_many_to_many(self):
        self.entry = Entry.objects.create(
            author=self.author,
            title="test header",
            content="Here is the content for Django tests")
        tag = Tag.objects.create(name="Developers")
        self.entry.tags.add(tag)
        self.assertEqual(self.entry.tags.count(), 1)
        self.assertIn(self.entry, tag.entries.all()) # type: ignore
    
