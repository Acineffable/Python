def consonantCounter(text):
  """Count the number of consonant in a word entered as string"""
  # Write the Function Body!
  consonant = 0
  list = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
  for letter in text:
    if letter in list:
      consonant = consonant + 1
  return consonant

consonantCounter("hello")
consonantCounter("Adios")
