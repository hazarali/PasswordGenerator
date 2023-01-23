import string as str
import random
digits=str.digits
upper_letters=str.ascii_uppercase
lower_letters=str.ascii_lowercase
ozel_karakterler=str.punctuation

my_pool=list(digits)+list(upper_letters)+list(lower_letters)+list(ozel_karakterler)
print(my_pool)
deneme= random.shuffle(my_pool)
print(my_pool)
print(my_pool[0:8])
my_password="".join(my_pool[0:8])
print(my_password)
