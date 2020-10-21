from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Announcement

def homeView(request):
	# user = User
	# user_list = User.objects.all()
	#paginator = Paginator(user_list, 10) # not yet implemented
	context = {
		'announcements': Announcement.objects.all().order_by("-date_posted"),
	}

	# template_folder/html_file
	return render(request, 'index/home.html', context)