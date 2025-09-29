from service.info import InfoService

client = "bigDogs"
conversation = "example"
info = InfoService(client, conversation)

base_message = [
    "Que vendes?",
    "Me das tu menú con todo y precios?",
    "Cuanto sería por dos aguas de jamaika?",
    "Entregas a domicilio?",
    "Te pido un pastori y una horchata"
]

for item in base_message:
    print(item)
    print(info.handle_conversation(item))