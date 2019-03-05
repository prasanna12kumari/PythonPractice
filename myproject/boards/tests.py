# from django.core.urlresolvers import reverse
from django.urls import reverse,resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .views import home,board_topics,new_topic
from .models import Board,Topic,Post
from .forms import NewTopicForm


# Create your tests here.
class HomeTests(TestCase):

	def setUp(self):
		self.board = Board.objects.create(name = 'Django',description = 'This is a Django discussion board')
		url = reverse('home')		
		self.response = self.client.get(url)
		
	def test_home_view_status_code(self):
				
		self.assertEquals(self.response.status_code,200)
		
	def test_home_url_resolves_home_view(self):
		view = resolve('/')		
		self.assertEquals(view.func,home)
	
	def test_home_view_contains_links_to_topics_page(self):
	
		board_topics_url = reverse('board_topics',kwargs = {'pk': self.board.pk})		
		self.assertContains(self.response,'href="{0}"'.format(board_topics_url))

class BoardTopicsTest(TestCase):
	
	def setUp(self):
		Board.objects.create(name='Django',description = 'This is a board about  Django')		
		
	def test_board_topics_success_status_code(self):
		
		url = reverse('board_topics',kwargs = {'pk':1})			
		response = self.client.get(url)		
		self.assertEquals(response.status_code,200)
	
	def test_board_topics_not_found_status_code(self):
	
		url = reverse('board_topics',kwargs = {'pk':99})
		response = self.client.get(url)
		self.assertEquals(response.status_code,404)
		
	def test_board_topics_urls_resolves_board_topics_views(self):				
		view = resolve('/boards/1/')		
		self.assertEquals(view.func,board_topics)
	
	 
	def test_board_topics_view_contains_navigation_links(self):
		board_topics_url = reverse('board_topics',kwargs = {'pk':1})
		home_page_url = reverse('home')
		new_topic_url = reverse('new_topic',kwargs = {'pk':1})
		response = self.client.get(board_topics_url)
		self.assertContains(response,'href="{0}"'.format(home_page_url))
		self.assertContains(response,'href = "{0}"'.format(new_topic_url))
		
		
		
		
class NewTopicsTest(TestCase):
	def setUp(self):
		Board.objects.create(name = "Django",description = "This is Django Discussion board")
		User.objects.create(username = "John",email = "john.doe@gmail.com",password = "123")
		
	def test_new_topic_success_status_code(self):
		url = reverse('new_topic',kwargs = {'pk':1})
		response = self.client.get(url)
		self.assertEquals(response.status_code,200)
	
	def test_new_topic_not_found_status_code(self):
		url = reverse('new_topic',kwargs = {'pk':99})
		response = self.client.get(url)
		self.assertEquals(response.status_code,404)
		
	def test_new_topic_view_resolves_new_topic_url(self):
		view = resolve('/boards/1/new/')
		self.assertEquals(view.func,new_topic)
		
	def test_new_topic_view_contains_link_back_to_board_topics_view(self):		
		new_topic_url = reverse('new_topic',kwargs = {'pk':1})			
		board_topics_url =  reverse('board_topics',kwargs = {'pk': 1})		
		response = self.client.get(new_topic_url)		
		self.assertContains(response,'href = "{0}"'.format(board_topics_url))
		
	def test_csrf(self):
		url = reverse('new_topic',kwargs = {'pk':1})
		response = self.client.get(url)
		self.assertContains(response,'csrfmiddlewaretoken')
	
	def test_new_topic_valid_post_data(self):
		url = reverse('new_topic',kwargs = {'pk':1})
		data ={'subject':'Test','message':'This is test topic'}
		response = self.client.get(url,data)
		self.assertTrue(response,Topic.objects.exists())
		self.assertTrue(response,Post.objects.exists())
	
	def test_new_topic_invalid_post_data(self):
		url = reverse('new_topic',kwargs = {'pk':1})
		response = self.client.post(url,{})
		form = response.context.get('form')
		self.assertEquals(response.status_code,200)
		self.assertTrue(form.errors)
	
	def test_new_topic_invalid_post_data_empty_field(self):
		url = reverse('new_topic',kwargs = {'pk':1})
		data ={'subject':'','message':''}
		response = self.client.get(url)
		self.assertTrue(response.status_code,200)
		self.assertFalse(Topic.objects.exists())
		self.assertFalse(Post.objects.exists())
	
	def test_contains_form(self):
		url = reverse('new_topic',kwargs ={'pk':1})
		response = self.client.get(url)
		form = response.context.get('form')
		self.assertIsInstance(form,NewTopicForm)
	