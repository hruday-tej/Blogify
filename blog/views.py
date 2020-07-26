from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import (ListView,
								 DetailView,
	  							CreateView)

# Create your views here.
def home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request,'blog/home.html',context)

def about(request):
	# return render(request,'blog/home.html')
	pass

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	# context_object_name = 'o'
	# template_name = 'blog/home.html'
	# context_object_name = 'posts'
	# ordering = ['-date_posted']
class PostCreateView(CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

