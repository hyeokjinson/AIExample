import re

r=re.compile('a.c')
print(r.search('abd'))
print(r.search('abc'))

r=re.compile("abc?")
print(r.search("abc"))
print(r.search("ab"))

r=re.compile("ab*c")
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbbc"))

r=re.compile("ab+c")
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbbc"))
r=re.compile("^bc")
print(r.search("abc"))
print(r.search("bc"))

r=re.compile("ab{2}c")
print(r.search("abc"))
print(r.search("abbc"))
print(r.search("abbbc"))

r=re.compile("ab{2,4}c")
print(r.search("abc"))
print(r.search("abbc"))
print(r.search("abbbc"))
print(r.search("abbbbc"))
print(r.search("abbbbbc"))

