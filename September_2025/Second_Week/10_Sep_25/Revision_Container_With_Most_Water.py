def max_water(height):
    if not height:
        return 0

    left = 0
    right = len(height)-1
    max_area = 0

    while left<right:
        width = right-left
        current_height = min(height[left]-height[right])
        area = width * current_height
        max_area = max(area,max_area)

        if height[left]<height[right]:
            left+=1

        else:
            right-=1

    return max_area




