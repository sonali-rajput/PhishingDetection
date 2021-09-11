from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-phishing-detection.zip'
}
auth_provider = PlainTextAuthProvider('sonalirajput1088@gmail.com', 'shutupBitxh*8')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider) #connect to cloud using user name, password, cloud_config file
session = cluster.connect()

row = session.execute("select release_version from system.local").one()#selects release_version from system.local on datastax cloud
if row:
    print(row[0])
else:
    print("An error occurred.")


rows = session.execute("INSERT INTO phishing.user_data (id,link,name) VALUES (4,'xyz.xyz','xyz'); ")#Insert data into the table
rows = session.execute('SELECT * FROM phishing.user_data')#Get data from the table


for row in rows:
    print(row[0],row[1],row[2])