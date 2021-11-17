#dictionary = changeable, unordered collection of key:value pairs
#FAST and can be access quickly

capitals = {'USA':'Washington DC',
            'India': 'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# print(capitals['Russia'])
# print(capitals.get('German'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)
