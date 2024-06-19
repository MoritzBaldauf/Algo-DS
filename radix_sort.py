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
        self.bucket_list_history.clear()  # clear history list at beginning of sorting
        # TODO

    # Helper functions

    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucket list and adds it to the bucket list history.
        @param bucket_list is your current bucket list, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)
        self.bucket_list_history.append(arr_clone)
