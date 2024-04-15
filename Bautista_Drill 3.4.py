def count_syllables(word):
  vowels = 'aeiouy'
  count = 0
  is_vowel = False

  for char in word.lower():
    if char in vowels:
      if not is_vowel: 
        count += 1
      is_vowel = True
    else:
      is_vowel = False

  if count == 0:
    return 1

  if word[-1] == 'e' and not any(char in vowels for char in word[:-1]):
    return count - 1

  return count

word = input("Enter a word: ")
syllables = count_syllables(word)
print(f"{word}: {syllables} syllable(s)")