class Solution:
    def run(self,array):
        try:
            letters = dict()

            for letter in set(array):
                count = 0
                for i in array:
                    if letter == i:
                        count +=1
                letters[letter]=count
            if self.check(letters):
                return "Yes"
            else:
                return "NO"
        except Exception as e:
            print(e)
    
    
    def check(self,letters):     
        try:
            if len((set(letters.values()))) ==1:
                return True
            elif len((set(letters.values()))) ==2:
                if list(set(letters.values()))[-1]-list(set(letters.values()))[0]==1:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
    
        
if __name__ == "__main__":
    test_case_1 = "abc"
    test_case_2 = "abccc"
    obj = Solution()
    print(f"Running Test case 1 {test_case_1} : {obj.run(test_case_1)}")
    print(f"Running Test case 2 {test_case_2} : {obj.run(test_case_2)}")