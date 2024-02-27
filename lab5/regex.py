from re import *;

f = open('row.txt', 'r');

# reg = compile('ab*')

txt = f.read();
# for line in txt:
#     res1 = reg.match(line)
#     if res1 != None:
#         print(res1.group())

#pl = "djnafsjdnfnb"


#1 task

x = match("ab*", txt)

#print(x);

#2 tast

b = match('ab{2,3}', txt);

#print(b);

#3 task 

c = findall('[a-z]+-[a-z]+', txt);

#print(c);

#4 task 

d = findall('[A-Z][a-z]+', txt);

#print(d);

#5 task

e = findall('a.*b$', txt);

#print(e);

#6 task

t = "dw.ad.asd,wds "

q = sub(",", ":", t)

q = sub('[.]', ':', q);

q = sub('[ ]', ':', q);

#print(q);

#7 task

p = "snake";

g = sub("snake", 'camel', p)

#print(g);

#8 task

r = 'AdscmAlemmNJWd'

n = split('[A-Z]', r)

#print(n);

#9 task

cnt = "SplitThisStringAtUppercaseLetters"

res = sub(r'([a-z])([A-Z])', r'\1 \2', cnt)

#print(res)

#10 task 

camel = "helloWorldExample"

snake_case = sub(r'([a-z])([A-Z])', r'\1_\2', camel)

#print(snake_case);