import pymongo
from pprint import pprint

from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}' \
      f'@cluster1.ss7fmb4.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.testDB

collection_products = db.products

# products = [
#     {
#         'title': 'bread2',
#         'price': 452,
#         'remains': 102,
#         'comment': 'no sugar',
#         'contain_gluten': True,
#     },
#     {
#         'title': 'soft drink2',
#         'price': 252,
#         'remains': 1002,
#         'comment': 'no sugar',
#         'contain_gluten': False,
#     },
#     {
#         'title': 'milk2',
#         'price': 152,
#         'remains': 12,
#         'comment': 'no sugar',
#         'contain_gluten': True,
#     },
#     {
#         'title': 'vinegar2',
#         'price': 252,
#         'remains': 102,
#         'comment': 'no sugar',
#         'contain_gluten': False,
#     },
# ]
#
# collection_products.insert_many(products)

# analog find
# query = []
# response = collection_products.aggregate(query)
# for doc in response:
#     print(doc)
# print(list(response))


# $match stage
# query = [{'$match': {'contain_gluten': False}}]
# response = collection_products.aggregate(query)
# pprint(list(response))

# query = [{'$match': {'$and': [  # $or
#       {'contain_gluten': False},
#       {'price': {'$gte': 50}},
# ]}}]
# response = collection_products.aggregate(query)
# pprint(list(response))


# $group stage
# query = [
#       {
#             '$group': {'_id': '$contain_gluten'}
#       }
# ]
# response = collection_products.aggregate(query)
# print(list(response))

# query = [
#       {
#             '$group': {'_id': {'gluten': '$contain_gluten', 'price': '$price'}}
#       }
# ]
# response = collection_products.aggregate(query)
# print(list(response))


# $sum stage
# query = [
#       {
#             '$group': {'_id': {'gluten': '$contain_gluten', 'price': '$price'}}
#       }
# ]
# response = collection_products.aggregate(query)
# print(list(response))
#
collection_products.drop()