import random
import string



def get_random_string(length: int) -> str:
  return ''.join(random.choices(string.ascii_letters + string.digits, k=length))