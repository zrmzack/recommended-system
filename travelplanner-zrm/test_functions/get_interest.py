from amadeus import Client, ResponseError

amadeus = Client(client_id="YhUHykQeccgseWSSARlxtfIAzhdGgTM2", client_secret="IWBwclckwNgBKNWr")
try:

    # What are the popular places in Barcelona (based a geo location and a radius)
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=41.397158, longitude=2.160873)
    print(response.data)

    # What are the popular places in Barcelona? (based on a square)
    resp = amadeus.reference_data.locations.points_of_interest.by_square.get(north=41.397158, west=2.160873,
                                                                             south=41.394582, east=2.177181)
    print(resp.data)


except ResponseError as error:
    print(error)
