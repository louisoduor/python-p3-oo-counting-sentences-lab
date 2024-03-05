#!/usr/bin/env python3

class MyString:
  def __init__(self, value =""):
    self.value = value

    if value is not str:
      print("The value must be a string.")
    else:
      self.value = value

  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    sentences = [sentence.strip() for sentence in sentences.split('[.!?]', self._value) if sentence.strip()]
    return len(sentences)
  
 
    
   