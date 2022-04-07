# Q1: Rate two strings between 0.0 - 1.0.
# If equal, then return 1.0
# If anagrams, then return 0.75
# If one letter difference, then return 0.50
# else return 0.0

# clariry questions: 
# (1) the string only contains alphabet? if so, are they all lowercase or may be upper case?
# (2) do the two strings have the same length?

class rate_two_strings:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        if len(self.str1) == len(self.str2):
            self.bucket1 = self._str_to_bucket(self.str1)
            self.bucket2 = self._str_to_bucket(self.str2)

    def compare_strs(self):
        if len(self.str1) != len(self.str2):
            return 0

        # if equal, return 1.0
        if self.str1 == self.str2:
            return 1.0

        # if anagrams, return 0.75
        if self.bucket1 == self.bucket2:
            return 0.75

        # if one letter difference, return 0.5
        if self.is_one_letter_difference():
            return 0.50

        return 0.0

    @staticmethod
    def _str_to_bucket(strx):
        # conver a string to a bucket list with 26 alphabet letter counts
        bucket = [0] * 26

        # count the frequency of the letters in the input string
        for letter in strx:
            bucket[ord(letter) - ord('a')] += 1

        return bucket

    def is_one_letter_difference(self):
        buckets_diff = [abs(l1 - l2) for l1, l2 in zip(self.bucket1, self.bucket2)]
        if sum(buckets_diff) == 2:
            return True
        else:
            return False


print(rate_two_strings('abbe', 'bbae').compare_strs()) # 1.0
# print(test.compare_strs('abc', 'bca')) # 0.75
# print(test.compare_strs('cdacdab', 'cdacdac')) # 0.50
# print(test.compare_strs('abcf', 'abze')) # 0.0
# print(test.is_one_letter_difference('abc', 'aaa'))


