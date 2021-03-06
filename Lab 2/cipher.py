import string

def caesar(plaintext, key):
	ciphertext = ""
	plaintext = plaintext.lower()
	for char in plaintext:
		newchar = ord(char) - 97 #convert character to it's ascii value minus 97 so a=0,b=1 etc
		newchar = (newchar + key) % 26 #add the key mod 26
		ciphertext += chr(newchar + 97) #convert back to a letter
	return ciphertext

def vigenere(plaintext, key):
	ciphertext = ""
	for i in range(len(plaintext)): #iterate through every letter
		ciphertext += caesar(plaintext[i],ord(key[i % len(key)])-97) #run caesar cipher on each letter with corresponding key letter as the key
	return ciphertext
	
print(caesar('ONEVARIATIONTOTHESTANDARDCAESARCIPHERISWHENTHEALPHABETISKEYEDBYUSINGAWORDINTHETRADITIONALVARIETYONECOULDWRITETHEALPHABETONTWOSTRIPSANDJUSTMATCHUPTHESTRIPSAFTERSLIDINGTHEBOTTOMSTRIPTOTHELEFTORRIGHTTOENCODEYOUWOULDFINDALETTERINTHETOPROWANDSUBSTITUTEITFORTHELETTERINTHEBOTTOMROWFORAKEYEDVERSIONONEWOULDNOTUSEASTANDARDALPHABETBUTWOULDFIRSTWRITEAWORDOMITTINGDUPLICATEDLETTERSANDTHENWRITETHEREMAININGLETTERSOFTHEALPHABETFORTHEEXAMPLEBELOWIUSEDAKEYOFRUMKINCOMANDYOUWILLSEETHATTHEPERIODISREMOVEDBECAUSEITISNOTALETTERYOUWILLALSONOTICETHESECONDMISNOTINCLUDEDBECAUSETHEREWASANMALREADYANDYOUCANTHAVEDUPLICATES',17))