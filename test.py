# from pymongo import client_options
# import pymongo
# import datetime 
# # from MongoOperations import MongoDBManagement



# # client = MongoDBManagement("mongodb159","mongodb159")

# # print(client)

# # print(client.isDatabasePresent("wisdomleaf"))

# # db = client.getDatabase('wisdomleaf')
# # print(db)
# # print(client.isCollectionPresent('appointment', db))


# mongo_client = pymongo.MongoClient("mongodb+srv://mongodb159:mongodb159@solar-system.meyls.mongodb.net/wisdomleaf")

# db = mongo_client['wisdomleaf']

# collection = db['appointment']
# # print("collection: ", collection)
# # db.collection.find({})

# # datetime.datetime.strptime("2021-04-25", "%Y-%m-%d")

# # res = db.collection.find({"startdate": 
# #                             {"$gte": datetime.datetime.strptime("2021-04-25", "%Y-%m-%d"),
# #                             "$lt": datetime.datetime.strptime("2021-05-25", "%Y-%m-%d")
# #                             }
# #                          })


# # print("db :", db)
# # print("collection : ",collection)                         

# # res = db.collection.find({
# #     "startdate": {
# #         "$gte": datetime.datetime.strptime("2021-04-25", "%Y-%m-%d"),
# #         "$lt": datetime.datetime.strptime("2021-05-25", "%Y-%m-%d")
# #     }
# # }).count()



# # res = collection.find({}, {
# #     "startdate":  datetime.datetime.strptime("2021-04-25", "%Y-%m-%d"),
# #     })



# # res = collection.find({}, {
# #     "title":1,
# #     "enddate":  {
# #         "&gte":"2021-04-20",
# #         "&lt":"2021-04-22"
# #     }
# #     })


# myquery = {
#             "$and": [       
#                         {"enddate":{"$gte":"2021-05-11"}},
#                         {"enddate":{"$lte":"2021-05-13"}}
#                     ]
#           }
            
#         #  { "$and": [ { price: { $ne: 1.99 } }, { price: { $exists: true } } ] } 


# res = collection.find(myquery, {"_id":0})
# # print([i for i in res])

# for i in res:
#     print(i)

# mongo_client.close()