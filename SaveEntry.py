class SaveEntry:

  def __init__(self):
    self.id = ""
    self.name = ""
    self.sourcePath = ""
    self.backupMethod = []

    def __init__(self, data):
      self.id = data.id
      self.name = data.name
      self.sourcePath = data.sourcePath
      self.backupMethod = data.backupMethod
    

  def __str__(self):
    return f"[{self.id}]{self.name}({self.sourcePath})\n{self.bkMethod}"

p1 = SaveEntry("John", 36)

print(p1.name)
print(p1.age)