# Non-relational databases - Practical

Apply the concepts learned about non-relational databases, using MongoDB and Compass.

## Deploy Flask app with Flask-PyMongo
● Create database Unit18 in Compass (Create Database)

● create virtual environment (venv)
```
python -m venv path\to\myenv
```
● Install requirements.txt dependencies
```
pip install -r requirements.txt 
```
● Run app
```
python app.py
```
● Running on 
```
http://localhost:8080
```
Go selecting from the first option to the last.

![Alt text](https://res.cloudinary.com/dimgzkmps/image/upload/v1669055333/flaskAp_ktkwyw.png)
![Alt text](https://res.cloudinary.com/dimgzkmps/image/upload/v1669056415/mongodb_qlldyg.png)
## Manual deploy
● Install MongoDB and Compass

● Create database Unit18 in Compass (Create Database)

![Alt text](https://res.cloudinary.com/dimgzkmps/image/upload/v1668463923/uni18_lntqpy.png)

● Accessing the database from step 2
```
use Unit18
```
● Access MongoDB from the console (ubuntu)
```
mongo
```

● Create two collections, customer and products
```
db.createCollection("customer")

db.createCollection("products")
```
Insert 1 documents in customer and products
```
db.customer.insertOne({_id:1,FullName:'Richard Doe',Level:1, Age:25, City:'Illinois', Zip:61061})

db.products.insertOne({_id:1, ProductName:'Iphone 8', Price:999, stock:10})
```

● Insert multiple documents with one command in collections
```
db.customer.insertMany([
	{_id:2,FullName:'Richard Doe', Level:1, Age:25, City:'Illinois', Zip:61061},
	{_id:3,FullName:'Mike Joe', Level:1, Age:32, City:'New York City', Zip:99999},
	{_id:4,FullName:'Arnold Stinson', Level:2, Age:29, City:'California', Zip:31061}])

db.products.insertMany([
	{_id:2, ProductName:'Sangsung Galaxy 10', Price:800, stock:5},
	{_id:3, ProductName:'Motorola Moto E20', Price:500, stock:3},
	{_id:4, ProductName:'Samsung Galaxy A13', Price:399, stock:2}])
```
● List existing documents in a collection
```
db.customer.find();

db.products.find();
```
● List a specific document within the collection
```
db.customer.find({_id:{$eq:1} })

db.products.find({_id:{$eq:2} })
```
● Update on a record in collections
```
db.customer.updateOne({_id:1},{$set:{FullName:'Robert Smith',Level:1, Age:33, City:'Illinois', Zip:61061} })

db.products.updateOne({_id:1},{$set:{Price:799} })
```
● Update to multiple records simultaneously.
```
db.customer.updateMany({_id:{$lte:2}},{$set:{Level:3} })

db.products.updateMany({_id:{$gte:2}},{$set:{stock:2} })
```
![Alt text](https://res.cloudinary.com/dimgzkmps/image/upload/v1668463936/mongo_fz68b4.png)
#### ● finally export .json files of both customer.json and products.json collections using compass into folder /json
