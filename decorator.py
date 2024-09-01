#Decorator code that measures how long it takes for a function to be executed 

import time

def decorator(func):
  def wrapper():
    start = time.time()
    func()
    end = time.time()
    time_taken = end - start
    print(f"time taken {time_taken}")
  return wrapper

def func():
  print("hello world")

timefn = decorator(func)
timefn()
