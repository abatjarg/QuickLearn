from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from models import Card
from forms import CardForm

#Lists all the cards
def list_cards(request):
	cards = Card.objects.all();
	context = {
		'cards':cards
	}
	return render(request, 'list_cards.html', context)

def show_card(request, pk=0):
	card = get_object_or_404(Card, pk=pk)
	context = {
		'card':card
	}
	return render(request, 'show_card.html', context)

def create_card(request):
	if request.method == "POST":
		formset = CardForm(data=request.POST)
		if formset.is_valid():
			formset.save()
			return redirect(to='list_cards')
	else:
		formset = CardForm()

	context = {
		'formset':formset
	}
	return render(request, 'create_card.html', context)

def delete_card(request, pk):
	Card.objects.filter(pk=pk).delete()
	return redirect(to='list_cards')

