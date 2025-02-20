class MyClass:
  def __enter__(self):
    print("Hello World!")
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    print("Hello, World!")

with MyClass() as mc:
    print("I'm in!")