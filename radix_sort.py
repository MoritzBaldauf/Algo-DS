class RadixSort:
    def __init__(self):
        self.base = 7
        self.bucket_list_history = []

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, input_array):
        """
        Sorts a given list using radix sort in descending order
        @param input_array to be sorted
        @returns a sorted list
        """

        self.bucket_list_history.clear() # clear history list at beginning of sorting

        if not input_array:
            return []

        max_digits = self.get_max_digits(input_array)

        previous_array = input_array[:]
        for digit in range(max_digits):
            buckets = self._bucket_sort(digit, input_array)
            input_array = self._merge(buckets)
            self._add_bucket_list_to_history(buckets)

        return input_array

    # Helper functions
    def _bucket_sort(self, pos, input_array):
        buckets = [[] for _ in range(self.base)]
        for number in input_array:
            bucket_index = self._get_digit(number, pos)
            buckets[-bucket_index-1].append(number)
        return buckets

    def _get_digit(self, val, pos):
        return (val // (10 ** pos)) % 10

    def get_max_digits(self, number):
        max_digits = 0
        temp_number = max(number)
        while temp_number > 0:
            temp_number //= 10
            max_digits += 1
        return max_digits

    def _merge(self, buckets):
        merged_list = []
        for i in range(self.base):
            merged_list.extend(buckets[i])
        return merged_list

    def _add_bucket_list_to_history(self, buckets):
        self.bucket_list_history.append([list(bucket) for bucket in buckets])