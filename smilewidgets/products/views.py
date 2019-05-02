from django.shortcuts import render
from rest_framework import status
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProductPrice, GiftCard, Product


class PriceCalculatorView(APIView):
 
	def get(self, request, *args, **kwargs):
		import pdb;pdb.set_trace()
		product_code = request.GET.get('productCode')
		fordate = request.GET.get('date')
		fordate = datetime.datetime.strptime(fordate, "%Y-%m-%d").date()
		try:
			gift_code = request.GET.get('giftCardCode')
		except:
			gift_code = None	
		#verify product
		try:
			product = Product.objects.get(code=product_code)
		except:
			return Response('Invalid Product Code')
		#Get product price
		foryear = fordate.year
		if foryear >= 2019:
			price_object = ProductPrice.objects.filter(offer_start_date__year=2019).filter(product__code=product_code)
		else:	
			price_object = ProductPrice.objects.filter(offer_start_date__lte=fordate,offer_end_date__gte=fordate).filter(product__code=product_code)		
		#verify gift code if any
		if len(price_object) > 0:
			product_price = price_object[0].product_price 
			if gift_code is not None:
				if product_price <= 0:
					return Response('Gift Card cannot be applied as price is already 0$ please remove gift card and try again')
				try:
					gift_object = GiftCard.objects.get(code=gift_code)
				except:
					Response('Invalid Gift Card Code')
				start_date = gift_object.date_start
				giftcode = gift_object.code
				end_date = gift_object.date_end
				if fordate<start_date:
					return Response('Offer Not yet started')
				if end_date != None:
					if fordate>end_date:
						return Response('Gift Code Expired')	
					elif(start_date-fordate <= start_date-end_date):
						product_price -= gift_object.amount
				else:
					product_price -= gift_object.amount
			product_price = '${0:.2f}'.format(product_price / 100)
			return Response({'FinalPrice': product_price})					 						
		else:
			return Response('Processing error')















# try:
# 	gift_object = GiftCard.objects.get(code=gift_code)
# except:
# 	Response('Invalid Gift Card Code')
# start_date = gift_object.start_date
# end_date = gift_object.end_date
# giftcode = gift_object.code
# if fordate<start_date:
# 	response('Offer Not yet started')
# elif fordate>end_date:
# 	response('Gift Code Expired')	
# elif(gift_objects.start_date-fordate <= start_date-end_date):
#         product_price -= gift_object.amount
# product_price -= gift_object.amount

