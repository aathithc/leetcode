class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        fill(image, sr,sc,color,image[sr][sc])
        return image

def fill(image, sr, sc, color, cur):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
        return
    if cur != image[sr][sc]:
        return
    if image[sr][sc] == color:
        return

    
    image[sr][sc] = color
    
    fill(image, sr-1,sc,color,cur)
    fill(image, sr+1,sc,color,cur)
    fill(image, sr,sc-1,color,cur)
    fill(image, sr,sc+1,color,cur)