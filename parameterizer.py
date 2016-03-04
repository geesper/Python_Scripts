#!/usr/bin/python

# Simple parameter reader for python scripts:
# 
# Initialize a parameterizer, then add parameters to it:
# p = parameterizer()
# p.add("-n", "Description of the -n value", False, False)
#
# Usage of add three required values and one optional value:
#   - parameter to look for, ex: -n
#   - description that can be displayed
#   - if the parameter is required to be present
#   - (Optional) if the parameter must have a value, rather than just being a switch: True = Must have a value
# 
#
# Once parameters have been added, you can check if they are present by using:
# p.present("-n")
#
# You can also get the value of the parameter by using:
# b.valueof("-n")

import sys

class parameterizer:
   def __init__(self):
      self.validparameters = []

   def add(self, param, description, required, value_required = True):
      temp = parameter(param, description, required, value_required)
      self.validparameters.append(temp)
      self.validate()

   def validate(self):
      for validparameter in self.validparameters:
         validparameter.validate(sys.argv)

   def present(self, value):
      for validparameter in self.validparameters:
         if validparameter.name == value:
            return validparameter.present
      return False

   def valueof(self, parameter_name):
      for validparameter in self.validparameters:
         if validparameter.name == parameter_name:
            return validparameter.value

   def noarguments(self):
      for validparameter in self.validparameters:
         if validparameter.present:
            return False 
      return True

class parameter:
   def __init__(self, name, description, required, value_required):
      self.name = name.lower()
      self.description = description
      self.value = ""
      self.required = required
      self.value_required = value_required
      self.present = False

   def validate(self, parameter_array):
      for index,item in enumerate(parameter_array):
         if item.lower() == self.name:
            if self.value_required:
               try:
                  self.value = parameter_array[index + 1]
                  self.present = True
                  break 
               except Exception, e:
                  print "Error iterating arguments! The following parameter is missing a value: %s " %(self.name)
                  sys.exit(1)
            else:
               self.present = True
               break
         if self.required and self.value == "" and self.value_required == True:
            print "Missing required parameter: %s (%s)" %(self.name, self.description)
            sys.exit(1)
