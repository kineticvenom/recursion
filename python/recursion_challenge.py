from string import ascii_letters, digits



def factorial(x):
	#base case 
	if x == 0:
		return 1
	return x * factorial(x-1)

valid_characters = set(ascii_letters + digits)
def palindrome(string):

	if len(string) <= 1:
		return True
	first = 0
	last = len(string) -1
	while string[first] not in valid_characters:
		first +=1
	while string[last] not in valid_characters:
		last -=1
	if first <= last and string[first] == string[last]:
		return palindrome(string[first+1:last])
	return False

def bottles(num):
	if not num:
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall...")
		return
	print(f"{num} {'bottle' if num == 1 else 'bottles'} of beer on the wall, {num} {'bottle' if num == 1 else 'bottles'} of beer.\nTake one down and pass it around, {num - 1} {'bottle' if num-1 == 1 else 'bottles'} of beer on the wall.")
	bottles(num-1)
		

romans_obj = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }
def roman_num(num,key=list(romans_obj.keys())):
	if not key:
		return ''
	count, num = divmod(num, romans_obj[key[0]])
	return key[0] * count + roman_num(num,key[1:])

