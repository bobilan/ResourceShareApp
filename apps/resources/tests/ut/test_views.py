from django.http import HttpResponseRedirect
from django.test import TestCase, Client
from django.urls import reverse
from apps.user.models import User
from apps.resources.models import Tag, Category, Resources


class TestResourcesView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_home_page_return_200_status(self):
        response = self.client.get(
            reverse("home_page"),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )

        self.assertEqual(response.status_code, 200)

    def test_home_page_user_cnt_0(self):
        user = User.objects.create_user(
            username="bo",
            password="OptionalPassword1010",
            first_name="Name",
            last_name="Last",
            email="email@example.com",
            bio="Good",
            title="Dev"

        )

        expected_user_cnt = 1

        response = self.client.get(
            reverse("home_page"),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )

        self.assertEqual(response.context["user_cnt"], expected_user_cnt)

    def test_home_page_view_resource_count(self):
        user = User.objects.create_user(
            username="bo",
            password="OptionalPassword1010",
            first_name="Name",
            last_name="Last",
            email="email@example.com",
            bio="Good",
            title="Dev"

        )

        # create a Tag
        tag = Tag(name="Python")
        tag.save()

        # create category
        category = Category(cat="SQL")
        category.save()

        # create Resource
        resource = Resources(
            user_id=user,
            cat_id=category,
            title="Pythonista",
            description="Neva",
            link="http://www.pythonista.",
        )
        # set the many to many relations for tag        resource.tags.add(tag)
        resource.save()

        expected_resources_cnt = 1

        response = self.client.get(
            reverse("home_page"),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )

        self.assertEqual(response.context["cnt"], expected_resources_cnt)

    def test_home_page_view_resource_per_category_count(self):
        # TODO check resource per category count
        pass

    def test_resource_detail_view_redirect_to_login_for_non_auth_user(self):
        response = self.client.get(
            reverse("resource-details", kwargs={'id': 1}),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )

        self.assertEqual(response.status_code, 302)

        self.assertIsInstance(response, HttpResponseRedirect)

    # def test_resource_detail_view_status_code_ok_for_aut_user(self):
    #     user = User.objects.create_user(
    #         username="bo",
    #         password="OptionalPassword1010",
    #         first_name="Name",
    #         last_name="Last",
    #         email="email@example.com",
    #         bio="Good",
    #         title="Dev"
    #
    #     )
    #
    #     # create a Tag
    #     tag = Tag(name="Python")
    #     tag.save()
    #
    #     # create category
    #     category = Category(cat="SQL")
    #     category.save()
    #
    #     # create Resource
    #     resource = Resources(
    #         user_id=user,
    #         cat_id=category,
    #         title="Pythonista",
    #         description="Neva",
    #         link="http://www.pythonista.",
    #     )
    #     # set the many to many relations for tag        resource.tags.add(tag)
    #     resource.save()
    #
    #     # login
    #     login = self.client.login(
    #         username="bo",
    #         password="OptionalPassword1010",
    #
    #     )
    #
    #     response = self.client.get(
    #         reverse("resource-details", kwargs={'id': 6}),
    #         HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
    #         HTTP_CONTENT_TYPE="",
    #     )
    #
    #     self.assertEqual(response.status_code, 200)


class TestUsersListView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_users_list_return_200_status(self):
        response = self.client.get(
            reverse("user_list"),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )

        self.assertEqual(response.status_code, 200)

    def test_users_list_empty_user_list(self):
        response = self.client.get(
            reverse("user_list"),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )
        self.assertEqual(len(response.context["users"]), 0)

    def test_users_list_non_empty_user_list(self):

        # Create one or more custom users
        custom_user1 = User.objects.create_user(
            username="bo",
            password="OptionalPassword1010",
            first_name="Name",
            last_name="Last",
            email="email@example.com",
            bio="Good",
            title="Dev"

        )

        custom_user2 = User.objects.create_user(
            username="bo2",
            password="OptionalPassword1010",
            first_name="Name1",
            last_name="Last1",
            email="email@example.com",
            bio="Good",
            title="Dev"
        )

        response = self.client.get(
            reverse("user_list"),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )
        breakpoint()

        users = response.context["users"]
        self.assertEqual(len(users), 2)
        self.assertIn(custom_user1, users)
        self.assertIn(custom_user2, users)

