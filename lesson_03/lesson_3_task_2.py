from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 13", "+79123336789"),
    Smartphone("Xiaomi", "Redmi", "+79234888890"),
    Smartphone("Samsung", "Galaxy 13", "+7933338901"),
    Smartphone("Poco", "One", "+79466689012"),
    Smartphone("Vivo", "10", "+79555555555")
]
for phone in catalog:
    print(f"{phone.type} - {phone.model}. {phone.phone_number}")
