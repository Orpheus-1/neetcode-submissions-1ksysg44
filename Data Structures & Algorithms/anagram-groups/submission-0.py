class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in counter:
                counter[sortedString] = []
            counter[sortedString].append(string)
        output = []
        # for sortedList in counter.values():
        #     output.append(sortedList)
        for key, sortedList in counter.items():
            output.append(sortedList)
        return output

