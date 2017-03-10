score = input("Inser your score:")

if score >= 90:
	credit = 'A'
elif score >= 80:
	credit = 'B'
elif score >= 70:
	credit = 'C'
elif score >= 60:
	credit = 'D'
else:
	credit = 'F'

print "Your credit is %s" % credit