import streamlit as st
import requests

BASE_URL = "http://localhost:5000/Product"

st.title("🚘Machio Product Management Dashboard")

menu = ["View Products", "Add Product", "Update Product", "Delete Product"]
choice = st.sidebar.selectbox("Select Action", menu)

# VIEW PRODUCTS
if choice == "View Products":
    st.subheader("📦 All Products")
    res = requests.get(BASE_URL)
    if res.status_code == 200:
        products = res.json()
        for prod in products:
            st.write(f"**ID:** {prod['id']}")
            st.write(f"**Name:** {prod['name']}")
            st.write(f"**Description:** {prod['description']}")
            st.write(f"**Price:** Ksh {prod['price']}")
            st.write(f"**Category:** {prod['cartegory']}")
            st.write(f"**In Stock:** {'✅ Yes' if prod['instock'] else '❌ No'}")
            st.divider()
    else:
        st.error("😔Failed to fetch products.")

# ADD PRODUCT
elif choice == "Add Product":
    st.subheader("➕ 🚘Add a New Product")
    id = st.number_input("Product ID", min_value=1)
    name = st.text_input("Name")
    description = st.text_area("Description")
    price = st.number_input("Price (Ksh)", min_value=0)
    cartegory = st.text_input("Category")
    instock = st.checkbox("In Stock")

    if st.button("Add Product"):
        data = {
            "id": id,
            "name": name,
            "description": description,
            "price": price,
            "cartegory": cartegory,
            "instock": instock
        }
        res = requests.post(BASE_URL, json=data)
        if res.status_code == 201:
            st.success("✅ Product added successfully!")
        else:
            st.error("❌😔 Failed to add product.")

# UPDATE PRODUCT
elif choice == "Update Product":
    st.subheader("🚘📝 Update a Product")
    prod_id = st.text_input("Enter Product MongoDB _id")
    price = st.number_input("New Price (Ksh)", min_value=0)
    description = st.text_area("New Description")
    instock = st.checkbox("In Stock?")
    
    if st.button("Update Product"):
        data = {"price": price, "description": description, "instock": instock}
        res = requests.put(f"{BASE_URL}/{prod_id}", json=data)
        if res.status_code == 200:
            st.success("✅🤝Product updated successfully!")
        else:
            st.error("❌ Update failed. Check Product ID.")

# DELETE PRODUCT
elif choice == "Delete Product":
    st.subheader("🗑️🚮 Delete a Product")
    prod_id = st.text_input("Enter Product MongoDB _id to Delete")

    if st.button("Delete Product"):
        res = requests.delete(f"{BASE_URL}/{prod_id}")
        if res.status_code == 200:
            st.success("✅ Product deleted successfully!")
        else:
            st.error("❌ Failed to delete product. Check ID.")
