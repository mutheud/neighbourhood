from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Profile,User,Post,Business,NeighborHood,Comment
from django.contrib.auth.models import User
import datetime as dt
from .forms import BusinessForm,ProfileForm,HoodForm,PostForm,CommentForm

# Create your views here.

def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day
    '''
    return render for home page
    '''
def home_page(request):
    date = dt.date.today()
    hoods = NeighborHood.objects.all()
    return render(request,'home.html',locals())

def logout(request):
    return render(request, 'home.html')

'''
    editing user profile fillform & submission
 
    '''
@login_required(login_url='/accounts/login/')
def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit_profile.html', locals())

@login_required(login_url='/accounts/login')
def upload_business(request):
    hood = NeighborHood.objects.get(id=request.user.profile.neighborhood.id)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            upload = businessform.save(commit=False)
            upload.user=request.user
            upload.neighborHood=request.user.profile.neighborhood
            upload.save()
        return redirect('hood',request.user.profile.neighborhood.id)
    else:
        businessform = BusinessForm()
    return render(request,'Business.html',locals())

@login_required(login_url='/accounts/login')
def add_hood(request):
    if request.method == 'POST':
        hoodform = HoodForm(request.POST, request.FILES)
        if hoodform.is_valid():
            upload = hoodform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home_page')
    else:
        hoodform = HoodForm()
    return render(request,'add_hood.html',locals())
    

@login_required(login_url='/accounts/login')
def join(request,neighborhood_id):
    hood = NeighborHood.objects.get(id=neighborhood_id)
    current_user = request.user
    current_user.profile.neighborhood = hood
    current_user.profile.save()
    return redirect('hood',neighborhood_id)

@login_required(login_url='/accounts/login')
def leave(request,neighborhood_id):
    current_user = request.user
    current_user.profile.neighborhood = None
    current_user.profile.save()
    return redirect('home_page')

@login_required(login_url='/accounts/login/')
def hood(request,neighborhood_id):
    current_user = request.user
    hood_name = current_user.profile.neighborhood
    single_hood = NeighborHood.objects.get(id = request.user.profile.neighborhood.id)
    # business=Business.objects.get(id = request.user.profile.neighborhood.id)
    comments = Comment.objects.all()
    form = CommentForm(instance=request.user)
    print(hood)

    return render(request,'hood.html',locals())

def one_post(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return render(request, 'commentspace.html', locals())
    return redirect('hood')

@login_required(login_url='/accounts/login')
def add_post(request):
    hood = NeighborHood.objects.get(id=request.user.profile.neighborhood.id)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.profile = request.user.profile
            post.user = request.user
            post.neighborHood=request.user.profile.neighborhood
            post.save()
            return redirect('hood',request.user.profile.neighborhood.id)
    else:
        postform = PostForm()
    return render(request,'add_post.html',locals())

@login_required(login_url='/accounts/login')
def search_results(request):
    business= Business.objects.all()
    hood = NeighborHood.objects.get(id=request.user.profile.neighborhood.id)
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())
