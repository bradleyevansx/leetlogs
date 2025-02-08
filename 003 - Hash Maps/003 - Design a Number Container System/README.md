## Design a Number Container System

**Difficulty**: `Medium` - **Tags**: `Hash Maps`, `Min Heap`

### Description

Design a number container system that can do the following:

    Insert or Replace a number at the given index in the system.
    Return the smallest index for the given number in the system.

Implement the NumberContainers class:

    NumberContainers() Initializes the number container system.
    void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
    int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.


### Examples

**Example 1:**

**Input**: ```["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]```

**Output**: ```[null, -1, null, null, null, null, 1, null, 2]```

### Constraints

- `1 <= index, number <= 10^9`

- `At most 10^5 calls will be made in total to change and find`

### Solution

```python
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
```

**Description**:

This solution is the typical double hash map solution to speed up querying. The only trick to this question is storing the indicies of the numbers in sorted order somehow. Leetcode suggests and ordered set, but I couldn't see one easily accessible in python so I used a min heap. The only slow part to this algorithm would be re-heapifying the indicies after removing one from the list. That is O(logn)

**Time Complexity**: O(logn) - **Space Complexity**: O(n) 

