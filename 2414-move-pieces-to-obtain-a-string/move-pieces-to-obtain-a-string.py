class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        s_idx, t_idx = 0, 0

        while s_idx < n or t_idx < n:
            # Skip all underscores in both strings
            while s_idx < n and start[s_idx] == '_':
                s_idx += 1
            while t_idx < n and target[t_idx] == '_':
                t_idx += 1

            # If both pointers reach the end, the strings are transformable
            if s_idx == n and t_idx == n:
                return True

            # If only one pointer reaches the end, transformation is impossible
            if s_idx == n or t_idx == n:
                return False

            # Check if characters don't match or violate movement rules
            if start[s_idx] != target[t_idx] or \
               (start[s_idx] == 'L' and s_idx < t_idx) or \
               (start[s_idx] == 'R' and s_idx > t_idx):
                return False

            # Move both pointers to the next character
            s_idx += 1
            t_idx += 1

        return True       