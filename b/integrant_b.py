import json

book ="""
{
  "book": [
    {
      "title": "Pinocho",
      "cover": "Dura",
      "year": "1923",
      "pages": "238"
    }
  ],
  "book1": [
    {
      "title": "Biblia",
      "cover": "Blanda",
      "year": "253",
      "pages": "753"
    }
  ],
  "book2": [
    {
      "title": "Principito",
      "cover": "Dura",
      "year": "1957",
      "pages": "348"
    }
  ],
   "book3": [
    {
      "title": "Principito",
      "cover": "Dura",
      "year": "1957",
      "pages": "348"
    }
  ]
}
"""


with open("json_b.json", 'w') as file:
    json.dump(book,file)

with open("json_b.json", 'r') as file:
    result = json.load(file)
    print(result)



