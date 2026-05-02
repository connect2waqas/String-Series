"""
TWO Most Important Function of String:
                                     1) ord()
                                     2) char()
                                     ord():
                                          this is a built-in function which return an integer representing.
                                          unicode for the given sting. 'a' --> U+0061 --> 97 --> 01100001.
                                                    for given integer its unicode integer value then its binary value.
                                        Syntax:
                                               ord(argument--> should be character and only one argument.)
                                               order("H")
                                               ord("a") to ord("z")--> 65 - 90
                                               ord("A) to ord("Z") --> 97-122
                                               So these integer are internally use to convert it to binary.
                                               let do some examples:"""
print(f"integer value for A: {ord("A")}")
print(f"integer value for B: {ord("B")}")
print(f"integer value for a: {ord("a")}")
print(f"integer value for b: {ord("b")}")
print("And so on...")
print(f"integer value from A - Z is range of : {ord("A")}-{ord("Z")}")
print(f"integer value from a - b is range of : {ord("a")}-{ord("b")}")
"""chr():
         it is reverse of ord() in which we will return the integer but in this now we will
         give an integer is an input and the function will return the character of that int.
   Syntax:
         chr(argument)
         Range should be 0 --> 1, 114, 111"""
print(f"character value for 97: {chr(65)}")
print(f"integer value for 66: {chr(66)}")
print(f"integer value for 97: {chr(97)}")
print(f"integer value for 98: {chr(98)}")
print("And so on...")
print(f"integer value from 65-90 is range of : {chr(65)}-{chr(90)}")
print(f"integer value from 97-98 is range of : {chr(97)}-{chr(98)}")
