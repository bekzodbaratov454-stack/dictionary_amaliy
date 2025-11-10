import os
os.system('cls')
students = {

	"Samandar": 18,
	"Muzaffar": 19,
	"Xojiakbar": 16,
	"Islom": 20,
	"Asomiddin": 14,
	"Sobitjon": 17,
	"Shoxruh": 20
}

for w in students:
    if students[w] >= 18:
        print(students[w] , w)

