prob = 0.2

probpos = 0.2 * 0.85
probnpos = 0.8 * 0.2
propo = probpos + probnpos

probgiven = 0.85

probresult = (prob*probgiven)/propo

print("person who will probably die is:", round(probresult),3)