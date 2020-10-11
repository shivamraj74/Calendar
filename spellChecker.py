from spellchecker import SpellChecker

spell=SpellChecker()

misspell=spell.unknown(['yuth','hevy','jav'])

for word in misspell:
  print(spell.correct.correction(word))
