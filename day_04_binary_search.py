"""
用While实现二分查找，并写单元测试确保正确
"""

def binary_search(array, target):
    if not array:
        return -1
    beg, end = 0, len(array)
    while beg <= end:
        mid = (end + beg) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            beg = mid + 1

    return -1


def test():
    """
    如何设计测试用例（等价类划分）
    -正常值功能测试
    -边界值（最大最小值、最左最右值）
    -异常值（比如None,空值，非法值）
    :return:
    """
    #正常值包含有无两种结果
    assert binary_search([1, 3, 5, 7, 9, 11, 13], 3) == 1
    assert binary_search([1, 3, 5, 7, 9, 11, 13], 9) == 4
    assert binary_search([1, 3, 5, 7, 9, 11, 13], 4) == -1

    #边界值
    assert binary_search([1, 3, 5, 7, 9, 11, 13], 1) == 0
    assert binary_search([1, 3, 5, 7, 9, 11, 13], 13) == 6

    #异常值
    assert binary_search([], 4) == -1

