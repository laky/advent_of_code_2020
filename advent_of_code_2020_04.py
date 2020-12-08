import re

def check_passport(passport):
	fields_to_check = [
		r"\bbyr\:((19[2-9][0-9])|(200[0-2]))\b",
		r"\biyr\:((2020)|(201[0-9]))\b",
		r"\beyr\:((2030)|(202[0-9]))\b",
		r"\bhgt\:((((19[0-3])|(1[5-8][0-9]))cm)|(((59)|(6[0-9])|(7[0-6]))in))\b",
		r"\bhcl\:(#[a-f0-9]{6})\b",
		r"\becl\:(amb|blu|brn|gry|grn|hzl|oth)\b",
		r"\bpid\:([0-9]{9})\b"
	]

	passport_valid = True
	for field in fields_to_check:
		m1 = re.findall(field, passport)
		m2 = re.findall(field.split(":")[0]+":", passport)
		passport_valid = passport_valid and (len(m1) == 1) and (len(m2) == 1)
	return passport_valid

with open("input_4_2.txt", "r") as f:
	passports = []
	passport = ""
	for line in f:
		line = line.strip()
		if line == "":
			passports.append(passport)
			passport = ""
		else:
			passport += line + " "
	passports.append(passport)

	count = 0
	for passport in passports:
		if check_passport(passport):
			count += 1
			
	print(count)
