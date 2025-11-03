# Crear un programa que censure determinadas palabras prohibidas

palabras_prohibidas = {'puerro', 'apio', 'brócoli'}

tweet = input('Introduce el texto del tweet:')
palabras_tweet = set(tweet.split())

if palabras_tweet.intersection(palabras_prohibidas):
    print('Has utilizado una palabra prohibida')
else:
    print('Eres un buen ciudadano')