class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()  # Sorting the merged array
        
        # Step 2: Find the median
        n = len(merged)
        if n % 2 == 1:  # Odd length
            return float(merged[n // 2])  # Middle element
        else:  # Even length
            mid1, mid2 = merged[n // 2 - 1], merged[n // 2]
            return (mid1 + mid2) / 2.0        