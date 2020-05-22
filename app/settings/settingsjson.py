
import json

settings_json = json.dumps([
    {'type': 'title',
     'title': ' Credentials'},
    {'type': 'bool',
     'title': 'A boolean setting',
     'desc': 'Boolean description text',
     'section': 'credentials',
     'key': 'boolexample'},
    {'type': 'numeric',
     'title': 'A numeric setting',
     'desc': 'Numeric description text',
     'section': 'credentials',
     'key': 'numericexample'},
    {'type': 'options',
     'title': 'An options setting',
     'desc': 'Options description text',
     'section': 'credentials',
     'key': 'optionsexample',
     'options': ['option1', 'option2', 'option3']},
    {'type': 'string',
     'title': 'A string setting',
     'desc': 'String description text',
     'section': 'credentials',
     'key': 'stringexample'},
])

  
