class NumberContainers:

    def __init__(self):
        self.numbersToIndex = {}       
        self.indexToNumber = {}       


    def change(self, index: int, number: int) -> None:
        if index in self.indexToNumber and self.indexToNumber[index] == number:
            return

        if number in self.numbersToIndex:
            heapq.heappush(self.numbersToIndex[number], index)
        else:
            self.numbersToIndex[number] = [index]
        if index in self.indexToNumber:
            oldNumber = self.indexToNumber[index]
            self.numbersToIndex[oldNumber].remove(index)
            if len(self.numbersToIndex[oldNumber]) == 0:
                del self.numbersToIndex[oldNumber]
            else:
                heapq.heapify(self.numbersToIndex[oldNumber])
        self.indexToNumber[index] = number
        

    def find(self, number: int) -> int:
        if number not in self.numbersToIndex:
            return -1
        return  self.numbersToIndex[number][0]