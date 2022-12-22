a="Python is a case  sensitive language"
#part a
print(len(a))
#part b
print(a[::-1])
#part c
word_1="a"
word_2="language"
start=a.find(word_1)
end=a.find(word_2)
result=slice(start,end)
result=a[result]
print("result",result)
#part d
part_d=a.replace("a case sentitive","object oriented")
print(part_d)
#part e
part_e=a.index("a")
print(part_e)
#part f
part_f=a.replace(" ","")
print(part_f)

