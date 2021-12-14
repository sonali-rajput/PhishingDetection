from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
    'secure_connect_bundle': 'cassandra\secure-connect-phishing-detection.zip'
}
auth_provider = PlainTextAuthProvider('sonalirajput1088@gmail.com', 'shutupBitxh*8')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

class data:
    def __init__(self,url,phishing):
        c = (session.execute('SELECT * FROM phishing.counter'))
        c = c[0][1]

        rows = session.execute("UPDATE phishing.counter set id_counter = {} where id = 1".format(c+1))
        try:
            rows = session.execute("INSERT INTO phishing.existing_url (id,phishing_value,url) VALUES ({},{},'{}'); ".format(c+1,phishing,url))

        except:
            rows = session.execute("UPDATE phishing.counter set id_counter = {} where id = 1".format(c))
            

# for row in rows:
#     print(row[0],row[1],row[2])

obj = data('youtube.com',1)