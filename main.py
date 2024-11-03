# Task 2
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


# Если нужно найти именно позицию для вставки
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1  # Ищем в правой половине
            else:
                right = mid  # Ищем в левой половине

        return left  # Возвращаем индекс для вставки



# ПОИСК ПИКА

class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


# Решение с учетом плато
def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Учитываем случай плато
        if nums[mid] == nums[mid + 1]:
            left += 1  # Продвигаем левую границу вправо
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1  # Двигаемся вправо
        else:
            right = mid  # Двигаемся влево

    return left  # or return right, since left == right here


print(findPeakElement([3, 3, 3, 3, 3, 3, 5, 1]))




# 33. Search in Rotated Sorted Array
# Устанавливаем два указателя left и right на начало и конец массива.
# Пока left меньше или равен right:
# Находим середину массива mid.
# Проверяем, если nums[mid] равен target. Если да, возвращаем mid.
# Если левая часть массива от left до mid отсортирована:
# Проверяем, находится ли target в пределах этой части, то есть, если nums[left] <= target < nums[mid]. Если да, перемещаем right в середину (right = mid - 1).
# В противном случае перемещаем left за середину (left = mid + 1).
# Если правая часть от mid до right отсортирована:
# Проверяем, находится ли target в пределах этой части, то есть, если nums[mid] < target <= nums[right]. Если да, перемещаем left за середину (left = mid + 1).
# В противном случае перемещаем right в середину (right = mid - 1).
# Если target не найден, возвращаем -1.
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Если нашли элемент, возвращаем его индекс
            if nums[mid] == target:
                return mid

            # Определяем, какая часть массива отсортирована
            if nums[left] < nums[mid]:  # Левая часть отсортирована
                # Проверяем, находится ли target в этой части
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Правая часть отсортирована
                # Проверяем, находится ли target в этой части
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1



# Дипломы
def can_fit(w, h, n, size):
    rows = size // w
    cols = size // h
    return rows * cols >= n

def min_board_size(w, h, n):
    left, right = 1, max(w, h) * n  # Определяем начальные границы бинарного поиска

    while left < right:
        mid = (left + right) // 2
        # Используем функцию can_fit для проверки
        if can_fit(w, h, n, mid):
            right = mid  # Если достаточно, ищем меньший размер
        else:
            left = mid + 1  # Если недостаточно, увеличиваем сторону доски

    return left  # Минимальный размер стороны

# Пример использования
w = 2
h = 3
n = 10
print(min_board_size(w, h, n))  # Output: 9