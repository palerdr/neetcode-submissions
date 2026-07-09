class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = [] #empty list to put unique numebrs into
        dupes = [] #list of dupes if not empty will return true
        for int in nums: # iterate through list
            if int not in uniques: 
                 uniques.append(int) #add if not already in uniques
            else:
                dupes.append(int)
        return dupes != []