#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.__value = value

  def get_value(self):
    return self.__value

  def set_value(self, value):
    if type(value) is str:
      self.__value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.__value[-1] == "."

  def is_question(self):
    return self.__value[-1] == "?"

  def is_exclamation(self):
    return self.__value[-1] == "!"

  def count_sentences(self):
    val = self.__value
    for punc_mark in ["!", "?"]:
      val = val.replace(punc_mark, '.')

    sentences = [s for s in val.split(".") if s]

    return len(sentences)
  
  value = property(get_value, set_value,)

p = MyString()
p.value = 123