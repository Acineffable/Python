def vowelCounter(text):
  """Count the number of vowels in a text entered as string"""
  vowel = 0
  for letter in text:
	  if letter in "aeiou" or "AEIOU":
		  vowel = vowel + 1
  return vowel
  print(vowel)

vowelCounter("hello")
vowelCounter("Adios")
