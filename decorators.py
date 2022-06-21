#Function that take another function as input functional programming
#loggin validations

def announce(f):
  def wrapper():
    print("About to run the function")
    f()
    print("Done with the function")
  return wrapper

@announce
def hello():
  print("hello World")

hello()
