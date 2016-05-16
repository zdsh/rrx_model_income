from pymongo import MongoClient

def get_mongo_db(db_name, host, port, user, passwd ):
    mongo = MongoClient(host, port)
    db = mongo[db_name]
    db.authenticate(user, passwd)
    return db

if __name__ == '__main__':
    db=get_mongo_db('rrx_xwdb', '10.10.159.15', 27017, 'rrx_xw', 'rrx_xw_pass')
    collection = db['xw_users']
    users = collection.find()
    for user in users:
        print( user )
        break
    