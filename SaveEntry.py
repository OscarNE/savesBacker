class SaveEntry:

  def __init__(self):
    self.name = ""
    self.path = ""
    self.bkMethod = []
    

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = SaveEntry("John", 36)

print(p1.name)
print(p1.age)