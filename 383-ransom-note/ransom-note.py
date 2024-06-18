class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = set(ransomNote) 
        for i in a:
            if magazine.count(i)<ransomNote.count(i):
              return(False)
              break
        
        else:
            return(True)