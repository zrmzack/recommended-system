from amadeus import Client, ResponseError 

amadeus = Client(
    client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
    client_secret='IWBwclckwNgBKNWr'
)


response = amadeus.shopping.hotel_offers.get(longitude=49.0, latitude=2.0)

print(response.data)

