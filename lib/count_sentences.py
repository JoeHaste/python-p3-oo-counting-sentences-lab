#!/usr/bin/env python3

class MyString:
  def __init__(self,value = ""):
    if issubclass(type(value), str):
      self.value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    punctuation_marks = ["!", ".", "?"]
    sentence_count = 0

    for char in self.value:
      if char in punctuation_marks:
        sentence_count += 1

    return sentence_count