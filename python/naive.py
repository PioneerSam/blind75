'''
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.
'''



class Solution:
    def simplifyPath(self, path: str) -> str:
        # first lets go through the string and replace all the "//" "///" with "/"
        # deal with "//"
        parts = path.split("//")
        print(parts)
        accum = ''
        for part in parts:
            accum += part + "/"
        path = accum[0:-1]

        # deal with "///"
        parts = path.split("///")
        print(parts)
        accum = ''
        for part in parts:
            accum += part + "/"
        path = accum[0:-1]

        # then split on "/" and reassemble the strings and return from right to left
        parts = path.split("/")
        parts = parts[::-1] # reverse it
        accum = ''
        skip_cnt = 0
        for part in parts:
            if part == "..":
                skip_cnt += 1
            elif part == ".":
                if skip_cnt > 0:
                    skip_cnt -= 1
                    continue
                continue
            else:
                if skip_cnt > 0:
                    skip_cnt -= 1
                    continue
                accum = '/' + part + accum

        accum = accum[1:-1]
        return accum
    


path = "/home//foo/"

s = Solution()
print(s.simplifyPath(path))


        


                


        
            
           

           
                

            

        





