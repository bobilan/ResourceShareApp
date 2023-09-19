from django.test import TestCase
from apps.resources import models
from apps.user.models import User
from apps.resources.models import Category


class TestTagModel(TestCase):
    def setUp(self) -> None:
        self.tag_name = "Python"
        self.tag = models.Tag(name=self.tag_name)

    def test_create_tag_object_success(self):
        self.assertIsInstance(self.tag, models.Tag)

    def test_dunder_str(self):
        self.assertEqual(str(self.tag), self.tag_name)


class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.category_name = "SQL"
        self.category = models.Category(cat=self.category_name)

    def test_create_category_object_success(self):
        self.assertIsInstance(self.category, models.Category)

    def test_dunder_str(self):
        self.assertEqual(str(self.category), self.category_name)

    def test_verbose_name_plural_set_correctly(self):
        verbose_name_plural = models.Category._meta.verbose_name_plural

        expected_name = "Categories"

        self.assertEqual(verbose_name_plural, expected_name)


class TestResourcesModel(TestCase):
    def setUp(self) -> None:

        self.user_id = User.objects.create_user(
            username="bo",
            password="OptionalPassword1010",
            first_name="Name",
            last_name="Last",
            email="email@example.com",
            bio="Good",
            title="Dev"

        )
        self.cat_id = Category.objects.create(cat="SQL")
        self.title = "Sample Resource"
        self.description = "This is a sample resource."
        self.link = "https://example.com/resource"
        self.resource = models.Resources(
            user_id=self.user_id,
            cat_id=self.cat_id,
            title=self.title,
            description=self.description,
            link=self.link,
        )

    def test_create_resources_object_success(self):
        self.assertIsInstance(self.resource, models.Resources)

    def test_dunder_str(self):
        expected_str = f"{self.resource.user_id.username} - {self.resource.title}"
        self.assertEqual(str(self.resource), expected_str)

    def test_username_property(self):
        self.assertEqual(self.resource.username, self.resource.user_id.username)

    def test_user_title_method(self):
        self.assertEqual(self.resource.user_title(), self.resource.user_id.title)


class TestResourcesTagModel(TestCase):
    def setUp(self) -> None:
        self.user_id = User.objects.create_user(
            username="bo",
            password="OptionalPassword1010",
            first_name="Name",
            last_name="Last",
            email="email@example.com",
            bio="Good",
            title="Dev"

        )
        self.cat_id = Category.objects.create(cat="SQL")
        self.title = "Sample"
        self.description = "This is a sample ."
        self.link = "https://example.com/resource"

        self.resources_id = models.Resources(
            user_id=self.user_id,
            cat_id=self.cat_id,
            title=self.title,
            description=self.description,
            link=self.link,
        )
        self.tag_id = models.Tag(name="Beginner")
        self.resources_tag = models.ResourcesTag(
            resources_id=self.resources_id, tag_id=self.tag_id
        )

    def test_create_resources_tag_object_success(self):
        self.assertIsInstance(self.resources_tag, models.ResourcesTag)


class TestReviewModel(TestCase):
    def setUp(self) -> None:
        self.user_id = User.objects.create_user(
            username="bo",
            password="OptionalPassword1010",
            first_name="Name",
            last_name="Last",
            email="email@example.com",
            bio="Good",
            title="Dev"

        )
        self.cat_id = Category.objects.create(cat="SQL")
        self.title = "Sample"
        self.description = "This is a sample ."
        self.link = "https://example.com/resource"

        self.resources_id = models.Resources(
            user_id=self.user_id,
            cat_id=self.cat_id,
            title=self.title,
            description=self.description,
            link=self.link,
        )
        self.tag_id = models.Tag(name="Beginner")
        self.resources_tag = models.ResourcesTag(
            resources_id=self.resources_id, tag_id=self.tag_id
        )

        self.body = "This is a review."
        self.review = models.Review(
            user_id=self.user_id, resources_id=self.resources_id, body=self.body
        )

    def test_create_review_object_success(self):
        self.assertIsInstance(self.review, models.Review)


class TestRatingModel(TestCase):
    def setUp(self) -> None:
        self.user_id = User.objects.create_user(
            username="bo",
            password="OptionalPassword1010",
            first_name="Name",
            last_name="Last",
            email="email@example.com",
            bio="Good",
            title="Dev"

        )
        self.cat_id = Category.objects.create(cat="SQL")
        self.title = "Sample"
        self.description = "This is a sample ."
        self.link = "https://example.com/resource"

        self.resources_id = models.Resources(
            user_id=self.user_id,
            cat_id=self.cat_id,
            title=self.title,
            description=self.description,
            link=self.link,
        )
        self.tag_id = models.Tag(name="Beginner")
        self.resources_tag = models.ResourcesTag(
            resources_id=self.resources_id, tag_id=self.tag_id
        )

        self.body = "This is a review."
        self.review = models.Review(
            user_id=self.user_id, resources_id=self.resources_id, body=self.body
        )

        self.rate = 4
        self.rating = models.Rating(
            user_id=self.user_id, resources_id=self.resources_id, rate=self.rate
        )

    def test_create_rating_object_success(self):
        self.assertIsInstance(self.rating, models.Rating)