def temperatura_media(cidades):
    medias = [(cidade[0], sum(cidade[1]) / len(cidade[1])) for cidade in cidades]
    return medias

cidades = [
    ("Cidade A", [30, 32, 31, 29, 28, 33, 31]),
    ("Cidade B", [25, 27, 26, 24, 23, 28, 29]),
]
medias = temperatura_media(cidades)
print(medias)
