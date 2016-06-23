class helpf():
  def loadListFromFile(self, file):
    List = []
    for i in file.readlines():
      List.append(i.split('\n')[0].lower())
    return(List)


help = helpf()