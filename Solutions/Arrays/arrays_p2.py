heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

#find length of list
print(len(heros))

#add black panther at end of list
heros.append('black panther')

# realize that you need to add black panther after hulk instead. fix it
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

#now you don't like thor and hulk so remove them and replace them with doctor strange
heros[1:3] = ["doctor strange"]
print(heros)