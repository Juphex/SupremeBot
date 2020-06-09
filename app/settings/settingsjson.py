import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'Credentials'},
    {'type': 'options',
     'title': 'Size',
     'desc': 'Size of Shirts, Trousers etc. that is to be bought if available',
     'section': 'credentials',
     'key': 'size',
     'options': ['Small', 'Medium', "Large", "XLarge"]},
  {'type': 'options',
     'title': 'Shorts-Size',
     'desc': 'Size of Shorts that is to be bought if available',
     'section': 'credentials',
     'key': 'shorts_size',
     'options': ['30', '32', "34", "36"]},
    {'type': 'string',
     'title': 'Name',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'name'},
     {'type': 'string',
     'title': 'E-mail',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'email'},
     {'type': 'string',
     'title': 'Telephone Number',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'tel'},
     {'type': 'string',
     'title': 'Street',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'street'},
     {'type': 'string',
     'title': 'Street number',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'street_nr'},
     {'type': 'string',
     'title': 'Address 3',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'address_3'},
     {'type': 'string',
     'title': 'City',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'city'},
     {'type': 'string',
     'title': 'Postal code',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'plz'},
     {'type': 'options',
     'title': 'Country',
     'desc': 'Needed in address formula',
     'section': 'credentials',
     'key': 'country',
     'options': ["UK","UK (N. IRELAND)", "AUSTRIA", "BELARUS", "BELGIUM", "BULGARIA", "CROATIA", "CZECH REPUBLIC",
     "DENMARK", "ESTONIA", "FINLAND", "FRANCE", "GERMANY", "GREECE", "HUNGARY", "ICELAND", "IRELAND",
     "ITALY", "LATVIA", "LITHUANIA", "LUXEMBOURG", "MONACO", "NETHERLANDS", "NORWAY", "POLAND", "PORTUGAL", 
     "ROMANIA", "RUSSIA", "SLOVAKIA", "SLOVENIA", "SPAIN", "SWEDEN", "SWITZERLAND", "TURKEY"]
     },
    {'type': 'title',
     'title': 'Payment Settings'},
    {'type': 'options',
     'title': 'Credit Card type',
     'desc': 'The bank your credit card is from',
     'section': 'payment',
     'key': 'credit_card_type',
     'options': ["Visa", "American Express", "Mastercard", "Solo"]},
     {'type': 'string',
     'title': 'Credit Card number',
     'desc': 'Needed in credit card formula',
     'section': 'payment',
     'key': 'credit_card_nr'},
    {'type': 'options',
     'title': 'Credit Card expiration month',
     'desc': 'Needed in credit card formula',
     'section': 'payment',
     'key': 'credit_card_exp_month',
     "options": ["01","02","03","04","05","06","07","08","09","10","11","12"]},
    {'type': 'options',
     'title': 'Credit Card expiration year',
     'desc': 'Needed in credit card formula',
     'section': 'payment',
     'key': 'credit_card_exp_year',
     "options": ["2020","2021","2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]},
    {'type': 'string',
     'title': 'CVV',
     'desc': 'Needed in credit card formula',
     'section' : 'payment',
     'key' : 'credit_card_cvv'}
])