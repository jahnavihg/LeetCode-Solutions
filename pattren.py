def getRow(self,rowIndex:int):
    if rowIndex == 0:
        return [1]
    prev = self.getRow(rowIndex)
    row=[1]
    for i in range(len(prev)-1):
        row.append(prev[i]+prev[i+1])
    row.append(1)
    return row