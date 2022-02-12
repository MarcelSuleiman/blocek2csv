from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import StreamingHttpResponse

from .forms import ReceiptUidManual

import csv
from .financna_sprava import over_doklad

# Create your views here.

def items_csv(request, uid):

	if uid == None:
		#data = check_recipt('O-318500C780EA418D8500C780EA018D95')
		pass
	else:
		#data = check_recipt(uid)
		data = over_doklad(uid)

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=items.csv'

		# create csv writer - excel friendly
		response.write(u'\ufeff'.encode('utf8'))
		writer = csv.writer(response, delimiter=';' , dialect='excel')

		writer.writerow(["Dátum a čas","Položka","Množstvo","Cena za MJ","Cena za MJ bez DPH","Cena celkom","Cena celkom bez DPH","DPH       ","Predajca","Predajca IČO","Predajca DIČ","Predajca IČ-DPH"])

		items = data['receipt']['items']

		date_of_purchase = data['receipt']['issueDate']
		seller = data['receipt']['organization']['name']
		ico = data['receipt']['organization']['ico']
		dic = data['receipt']['organization']['dic']
		ic_dph = data['receipt']['organization']['icDph']

		for item in items:

			item_name = item['name'].split(' ')
			count = item_name.count('')
			for i in range(count):
				item_name.remove('')

			item_name = ' '.join(item_name)

			quantity = str(item['quantity']).replace('.', ',')
			price_per_all = str(round(item['price'], 2)).replace('.', ',')

			ppo = item['price'] / item['quantity']
			price_per_one = str(round(ppo, 2)).replace('.', ',')
			
			vat_rate = str(item['vatRate']).replace('.', ',')

			price_per_one_without_dph = ppo / ((item['vatRate'] + 100) / 100)
			price_per_one_without_dph = str(round(price_per_one_without_dph, 2)).replace('.', ',')

			price_per_all_without_dph = item['price'] / ((item['vatRate'] + 100) / 100)
			price_per_all_without_dph = str(round(price_per_all_without_dph, 2)).replace('.', ',')

			writer.writerow([date_of_purchase, item_name, quantity, price_per_one, price_per_one_without_dph,\
				price_per_all, price_per_all_without_dph, vat_rate, seller, ico, dic, ic_dph])
		
			#print(date_of_purchase, item_name, quantity, price_per_one, price_per_all, vat_rate, seller, ico, dic, ic_dph)

		return response

def home(request):

	form = ReceiptUidManual
	if request.method == 'POST':
		form = ReceiptUidManual(request.POST)

		if form.is_valid():

			print(form.cleaned_data['receipt_uid'])

			uid = form.cleaned_data['receipt_uid']
			len_uid = len(uid)

			if len_uid != 34:
				print('Nesprávny počet znakov, valídny UID musí mať 34 znakov.')
				messages.success(request, f'Nesprávny počet znakov, valídny UID musí mať 34 znakov. Zadal si {len_uid} znakov dlhý reťazec.')

			else:
				redirect_url = 'export/'+str(uid)
				return redirect(redirect_url)

	return render(request, 'home.html', {'form':form})