from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm, SearchForm, EditClient
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

  
# @login_required
def index(request):
	clients = Client.objects.all().order_by("renewal_date")
	print(clients)
	clients = Client.objects.filter(created_by=request.user).order_by("renewal_date")
	return render(request, "clients/index.html", {
		"clients": clients
	})


# @login_required
def register(request):
	if request.method == "POST":
		form = ClientForm(request.POST)
		# print(form.created_by)
		if form.is_valid():
			client = form.save(commit=False)
			client.created_by = request.user
			client.save()
			return HttpResponseRedirect(reverse('clients:register'))
		else:
			print(form.cleaned_data, request.user)
			return render(request, "clients/register.html", {
				"message": "error: failed to add client"
			})
	else:
		form = ClientForm()
		return render(request, "clients/register.html", {
			"form": form
		})


# @login_required
def search_view(request):
	form = SearchForm(request.GET or None)
	results = []
	message = [' ']
	if request.method == 'GET' and form.is_valid():
			category = form.cleaned_data['category']
			query = form.cleaned_data['query']
			results = search(request, category, query)
			print(len(results))
	else:
		try:
			query_lenth = len(form.cleaned_data['query'])
		except (AttributeError, KeyError):
			return render(request, 'clients/search.html',
				{'form': form, 'results': results,}
			)
	if len(results) == 0:
		message[0] = 'client not found: review search query and try again'

	print(results)
	return render(request, 'clients/search.html', 
			   {'form': form, 'results': results, 'message': message[0],}
			   )

def search(request, category, query):
	search_filters = {
		'name': {'name__icontains': query},
		'registration_number': {'registration_number__icontains': query},
		'policy_number': {'policy_number__icontains': query},
		'created_by': {'created_by': request.user}
	}

	filter_kwargs = search_filters.get(category, {})
	results = Client.objects.filter(**filter_kwargs) if filter_kwargs else message

	return results


# @login_required
def client_details(request, client_id):
	client = Client.objects.filter(id=client_id, created_by=request.user) if client_id else None
	return render(request, 'clients/client_details.html', {'client': client})


# @login_required
def edit_client(request, client_id):
	client = get_object_or_404(Client, id=client_id, created_by=request.user)
	if request.method == 'POST':
		form = EditClient(request.POST, instance=client)
		if form.is_valid():
			print('is valid')
			form.save()
			return redirect('clients:index')
	else:
		form = ClientForm(instance=client)
	return render(request, 'clients/edit.html',
		{'form': form, 'client': client,

	})


# @login_required
def delete_client(request, pk):
	client = get_object_or_404(Client, pk=pk, created_by=request.user)
	if request.method == 'POST':
		client.delete()
		messages.success(request, "The client was deleted successfully.")
		return redirect('clients:index')
	return render(request, 'clients/edit.html', {'client': client})


