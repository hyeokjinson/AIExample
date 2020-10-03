#upper()
#lower()
#capitalize()
#title
#swapcase()

text="hello"
upper_text=text.upper()
print(upper_text)

lower_text=text.lower()
print(lower_text)

sentence='hello python'
capitalize_sentence=sentence.capitalize()
print(capitalize_sentence)

title_sentence=sentence.title()
print(title_sentence)

swap_sentence=title_sentence.swapcase()
print(swap_sentence)
print("---------------------------------------------------------------------------------")

text=' hello python '
print(text.strip())
print(text.rstrip())
print(text.lstrip())

print(text.replace(' ','.'))
print(text.replace('hello','bye'))

print("---------------------------------------------------------------------------------")
test='hellow python\n this is nlp tutorial\n string function examples\n'
print(test)
print(test.split('\n'))
print("---------------------------------------------------------------------------------")
#검색

text='hi hi2 hi3 hi4'
print(text.count('hi'))
print(text.find('hi'))
print(text.find('hi',1))
print(text.rfind('hi'))