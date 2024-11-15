import streamlit as st

# Crear una lista de productos con iconos simulados
products = {
    1: {"name": "Milk", "icon": "🥛"},
    2: {"name": "Bread", "icon": "🍞"},
    3: {"name": "Apples", "icon": "🍎"},
    4: {"name": "Eggs", "icon": "🥚"},
    5: {"name": "Cereal", "icon": "🥣"}
}

st.title("SmartShop Buddy - Virtual Shopping Assistant")

user_input = st.text_input("Say 'Add' followed by the item number to add to your shopping list:")
shopping_list = []

if user_input.startswith("Add") and user_input.split(" ", 1)[1].isdigit():
    item_number = int(user_input.split(" ", 1)[1])
    if item_number in products:
        shopping_list.append(products[item_number]["name"])
        st.write(f"Added {products[item_number]['icon']} {products[item_number]['name']} to your shopping list")
    else:
        st.write("Invalid item number. Please try again.")

st.write("## Shopping List:")
for index, item in enumerate(shopping_list, start=1):
    st.write(f"{index}. {item}")

st.write("## Products:")
for number, product in products.items():
    st.write(f"{number}. {product['icon']} {product['name']}")