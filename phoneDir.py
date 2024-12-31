# Time:O(n) 
# Space:O(n) for set and deque
# Leetcode: Yes
# Issues:None


from collections import deque
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.used = set()                   # used phone numbers
        self.q = deque()                    # usable phone numbers

        for i in range(maxNumbers):         # add usable numbers to queue O(n)
            self.q.append(i)

    def get(self) -> int:                   
        if not self.q: return -1            # queue is empty O(1)
        curr = self.q.popleft()             
        self.used.add(curr)                 # number is now in use
        return curr

    def check(self, number: int) -> bool:   # O(1)
        return number not in self.used      

    def release(self, number: int) -> None:
        if number not in self.used:         # O(1)                                
            return None
        self.used.remove(number)            # number not in use can be assigned
        self.q.append(number)
        return number



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)