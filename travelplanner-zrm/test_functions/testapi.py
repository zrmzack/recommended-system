from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
    client_secret='IWBwclckwNgBKNWr'
)
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='SYD',
        destinationLocationCode='BKK',
        departureDate='2020-07-01',
        adults=1)
    print(response.data)
except ResponseError as error:
    print(error)