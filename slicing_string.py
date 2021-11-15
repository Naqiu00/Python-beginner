#string slicing = create substring from another sting by extracting the elements
#indexing[] or slice()
#[start:stop:step]

name = "Chris Patt"

first_name = name[0:5]
# or
first_name = name[:5]
print(first_name)

last_name = name[6:]
print(last_name)

trash_name = name[::2]
print(trash_name)

reversed_name = name[::-1]
print(reversed_name)

website = "https://youtube.com"

slice = slice(8,-4,1)
print(website[slice])