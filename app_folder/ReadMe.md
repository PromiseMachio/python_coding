# 🚗 Machio Product API

A simple **RESTful API** built using **Node.js**, **Express**, and **MongoDB (Mongoose)**.  
This API allows you to **create, read, update, and delete** products from a MongoDB database.

---

## 🧾 Description

Each product in the database contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | Number | Unique product ID |
| `name` | String | Name of the product |
| `description` | String | Short description of the product |
| `price` | Number | Price of the product |
| `cartegory` | String | Product category (e.g. Sedan, SUV, Truck) |
| `instock` | Boolean | Availability status (true/false) |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone express-js-server-side-framework-PromiseMachio.git
cd MyWeek2_Assignment
```

## 2️⃣ Install Dependencies
```bash
npm install
```
## 3️⃣ Create a .env File

Inside the project root, create a .env file and add the following:
```json
PORT=5000
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/products
```
## 4️⃣ Run the Server

For production:
```bash
    
npm start

```
For development (using nodemon):
```bash
nodemon server.js
```

Once running, visit:
👉 http://localhost:5000/product

---

##🧩 API Endpoints
###🔹 GET /Product

Description: Fetch all products in the database.

Result_after_posting:
```json
[
    {
        "_id": "68e9155a2225875c9e3c7858",
        "id": 1,
        "name": "Toyota Corolla",
        "description": "Reliable and fuel-efficient compact sedan",
        "price": 1800000,
        "cartegory": "Sedan",
        "instock": true,
        "createdAt": "2025-10-10T14:16:58.850Z",
        "updatedAt": "2025-10-10T14:16:58.850Z",
        "__v": 0
    },
    {
        "_id": "68e9159b2225875c9e3c785a",
        "id": 2,
        "name": "Honda Civic",
        "description": "Stylish and efficient with advanced safety features",
        "price": 1900000,
        "cartegory": "Sedan",
        "instock": true,
        "createdAt": "2025-10-10T14:18:03.328Z",
        "updatedAt": "2025-10-10T14:18:03.328Z",
        "__v": 0
    },
    {
        "_id": "68e915ab2225875c9e3c785c",
        "id": 3,
        "name": "Mazda CX-5",
        "description": "Comfortable and sporty SUV with sleek design",
        "price": 3200000,
        "cartegory": "SUV",
        "instock": true,
        "createdAt": "2025-10-10T14:18:19.241Z",
        "updatedAt": "2025-10-10T14:18:19.241Z",
        "__v": 0
    },
    {
        "_id": "68e915b92225875c9e3c785e",
        "id": 4,
        "name": "Nissan X-Trail",
        "description": "Spacious SUV perfect for family travel",
        "price": 3100000,
        "cartegory": "SUV",
        "instock": false,
        "createdAt": "2025-10-10T14:18:33.290Z",
        "updatedAt": "2025-10-10T14:18:33.290Z",
        "__v": 0
    },
    {
        "_id": "68e915cd2225875c9e3c7860",
        "id": 5,
        "name": "Subaru Forester",
        "description": "All-wheel drive SUV with advanced traction control",
        "price": 3300000,
        "cartegory": "SUV",
        "instock": true,
        "createdAt": "2025-10-10T14:18:53.676Z",
        "updatedAt": "2025-10-10T14:18:53.676Z",
        "__v": 0
    },
    {
        "_id": "68e915df2225875c9e3c7862",
        "id": 6,
        "name": "BMW 320i",
        "description": "Luxury sedan with smooth performance and tech features",
        "price": 7500000,
        "cartegory": "Luxury",
        "instock": true,
        "createdAt": "2025-10-10T14:19:11.337Z",
        "updatedAt": "2025-10-10T14:19:11.337Z",
        "__v": 0
    },
    {
        "_id": "68e915eb2225875c9e3c7864",
        "id": 7,
        "name": "Mercedes-Benz C-Class",
        "description": "Premium car combining comfort and power",
        "price": 8500000,
        "cartegory": "Luxury",
        "instock": false,
        "createdAt": "2025-10-10T14:19:23.062Z",
        "updatedAt": "2025-10-10T14:19:23.062Z",
        "__v": 0
    },
    {
        "_id": "68e916002225875c9e3c7866",
        "id": 8,
        "name": "Volkswagen Golf GTI",
        "description": "Hot hatchback with sporty performance and sharp handling",
        "price": 4200000,
        "cartegory": "Hatchback",
        "instock": true,
        "createdAt": "2025-10-10T14:19:44.205Z",
        "updatedAt": "2025-10-10T14:19:44.205Z",
        "__v": 0
    },
    {
        "_id": "68e916102225875c9e3c7868",
        "id": 9,
        "name": "Audi Q5",
        "description": "Luxury mid-size SUV offering smooth handling",
        "price": 8700000,
        "cartegory": "Luxury SUV",
        "instock": true,
        "createdAt": "2025-10-10T14:20:00.645Z",
        "updatedAt": "2025-10-10T14:20:00.645Z",
        "__v": 0
    },
    {
        "_id": "68e916272225875c9e3c786a",
        "id": 10,
        "name": "Ford Ranger",
        "description": "Durable and powerful pickup truck for work and adventure",
        "price": 4500000,
        "cartegory": "Pickup",
        "instock": true,
        "createdAt": "2025-10-10T14:20:23.056Z",
        "updatedAt": "2025-10-10T14:20:23.056Z",
        "__v": 0
    },
    {
        "_id": "68e916372225875c9e3c786c",
        "id": 11,
        "name": "Toyota Land Cruiser",
        "description": "Strong off-road SUV with long-lasting performance",
        "price": 12000000,
        "cartegory": "SUV",
        "instock": true,
        "createdAt": "2025-10-10T14:20:39.449Z",
        "updatedAt": "2025-10-10T14:20:39.449Z",
        "__v": 0
    },
    {
        "_id": "68e916452225875c9e3c786e",
        "id": 12,
        "name": "Tesla Model 3",
        "description": "Electric sedan with autopilot and long range",
        "price": 9000000,
        "cartegory": "Electric",
        "instock": false,
        "createdAt": "2025-10-10T14:20:53.447Z",
        "updatedAt": "2025-10-10T14:20:53.447Z",
        "__v": 0
    },
    {
        "_id": "68e916522225875c9e3c7870",
        "id": 13,
        "name": "Mitsubishi Outlander",
        "description": "Stylish family SUV with hybrid option",
        "price": 3400000,
        "cartegory": "SUV",
        "instock": true,
        "createdAt": "2025-10-10T14:21:06.808Z",
        "updatedAt": "2025-10-10T14:21:06.808Z",
        "__v": 0
    }
]
```
---

## 🔹 PUT /Product/:id

Description: Update a product by its ID.
id to be updated:http://localhost:5000/Product/68e915b92225875c9e3c785e
```json
 {
  "price": 2700000,
  "instock": false
}
```
Result
```json
{
    "_id": "68e915b92225875c9e3c785e",
    "id": 4,
    "name": "Nissan X-Trail",
    "description": "Spacious SUV perfect for family travel",
    "price": 2700000,
    "cartegory": "SUV",
    "instock": false,
    "createdAt": "2025-10-10T14:18:33.290Z",
    "updatedAt": "2025-10-10T14:37:36.635Z",
    "__v": 0
}
```

id updated:http://localhost:5000/Product/68e915df2225875c9e3c7862
```json
 {
  "description":"Luxury sedan with smooth performance, tech features and additional MVC and multi_carbon turbo nitrous",
  "price": 5700000,
  "instock": false
}
```
```json
{
    "_id": "68e915df2225875c9e3c7862",
    "id": 6,
    "name": "BMW 320i",
    "description": "Luxury sedan with smooth performance, tech features and additional MVC and multi_carbon turbo nitrous",
    "price": 5700000,
    "cartegory": "Luxury",
    "instock": false,
    "createdAt": "2025-10-10T14:19:11.337Z",
    "updatedAt": "2025-10-10T14:44:45.219Z",
    "__v": 0
}
```

---

## 🔹 DELETE /Product/:id

Description: Delete a product by its ID.
id to be deleted:http://localhost:5000/Product/68e916002225875c9e3c7866
```json
{
    "message": "Deleted succesfully..."
}
```
---
## 🧠 Notes
- Ensure MongoDB Atlas or your local MongoDB server is running before starting the app.

- Use Postman or Insomnia to test API endpoints.

- Validation is handled automatically by Mongoose Schema.

- The project uses express.json() middleware to parse incoming JSON data.

## 👨‍💻 Author

### Machio Promise Arauna
📧 Email: machiopromise05@gmail.com

🐙 GitHub: https://github.com/PromiseMachio
