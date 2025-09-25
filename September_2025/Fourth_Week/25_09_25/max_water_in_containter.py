def max_water_in_container(height):
    if not height:
        return 0

    max_area = 0
    left = 0
    right = len(height)-1

    while left<right:
        width = right-left
        area = min(height[left],height[right])

        current_area = width * area

        max_area = max(max_area,current_area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(max_water_in_container(height))


