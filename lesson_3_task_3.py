from address import Address
from mailing import Mailing
to_address = Address("123456", "Волгово", "Лунная", "10", "15")
from_address = Address("654321", "Выборг", "Терский", "5", "15")
mailing = Mailing(to_address, from_address, 500, "TRACK123456")
print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - "
      f"{mailing.from_address.apartment} в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
