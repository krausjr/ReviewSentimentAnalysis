#this project displays five star google reviews for James Kraus while employed at Scheller's Fitness and Cycling.

# import json
# from outscraper import ApiClient

# api_cliet = ApiClient(api_key='')
# business_with_reviews = api_cliet.google_maps_business_reviews(
#     'https://www.google.com/maps/place/Schellers+Fitness+%26+Cycling+-+Middletown/@38.2451812,-85.544778,17z/data=!3m1!4b1!4m5!3m4!1s0x88699f4ed08a1b7f:0x5f9c01ca3e993ec8!8m2!3d38.2452996!4d-85.5425872',
#     limit=1,
#     language='en'
# )

# with open('reviews.json', 'w') as file:
#     json.dump(business_with_reviews, file, indent=4)

from outscraper import ApiClient

api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMDY1MTkyNjg3MzQzNTY2MDc2NzV8YjcxOTIzMmFhMw')

# Get reviews of the specific place by id
result = api_client.google_maps_reviews('https://www.google.com/maps/place/Schellers+Fitness+%26+Cycling+-+Middletown/@38.2451812,-85.544778,17z/data=!3m1!4b1!4m5!3m4!1s0x88699f4ed08a1b7f:0x5f9c01ca3e993ec8!8m2!3d38.2452996!4d-85.5425872', reviewsLimit=1, language='en')
print(result)

# Get reviews for places found by search query
# result = api_client.google_maps_reviews('Memphis Seoul brooklyn usa', reviewsLimit=20, limit=500, language='en')

# Get only new reviews during last 24 hours
# from datetime import datetime, timedelta
# yesterday_timestamp = int((datetime.now() - timedelta(1)).timestamp())

# result = api_client.google_maps_reviews(
#     'ChIJrc9T9fpYwokRdvjYRHT8nI4', sort='newest', cutoff=yesterday_timestamp, reviewsLimit=100, language='en')
