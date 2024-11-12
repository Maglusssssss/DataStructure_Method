from re import I


def find_minimum_sum(nums):
    """
    Tìm đỉnh núi có tổng nhỏ nhất.
    Cho một danh sách số nguyên dương nums
    Bộ 3 chỉ số i, j, k được gọi là đỉnh núi nếu thỏa mãn:
    i < j < k và nums[i] < nums[j] và nums[j] > nums[k]
    Ví dụ 1: input [8,6,1,5,3]
    với i = 2, j = 3 k = 4 tương ứng tạo thành một đỉnh núi với tổng bằng 9 (1 + 5 + 3)
    output: 9
    Ví dụ 2: input [5,4,8,7,10,2]
    i = 0, j = 2, k = 5 tạo thành một đỉnh núi với tổng bằng 15.
    i = 1, j = 4, k = 5 tạo thành một đỉnh núi với tổng bằng 16.
    output : 13
    Nếu không tồn tại đỉnh núi nào trong danh sách
    output : -1
    """
    for i in range(0,len(nums)-1):
        for j in range(i,len(nums)-1):
            for k in range(j,len(nums)-1):
                if nums[i] < nums[j] and nums[j] > nums[k]:
                    return sum(nums[i] + nums[j] + nums[k])
    return -1

x = [5,4,8,7,10,2]
print(find_minimum_sum(x))
