# Problem 1
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class TwoSum:

    @staticmethod
    def get_indices(numbers_array, target_sum):
        """
        Returns 2 indices in the array whose values add up to the target sum.
        If none are found, it returns [-1, -1]
        :param numbers_array: List[int]
        :param target_sum: int
        :return indices: List[int]
        """

        # Map to keep track on numbers already seen
        # key = number, value = index
        seen = dict()

        for idx, val in enumerate(numbers_array):
            need = target_sum - val
            if need in seen.keys():
                return [seen[need], idx]
            seen[val] = idx

        return [-1, -1]


print(TwoSum.get_indices([2, 7, 11, 15], 9))
print(TwoSum.get_indices([7, 3, 4, 2], 5))
print(TwoSum.get_indices([1, 3, 4, 2], 8))
