class Solution:
    def simplifyPath(self, path: str) -> str:
        # have a stack that stores the dir names
        # you get the dir name using a while loop b/w two slashes or EOS
        # if the dir added is a "..", pop the stack twice
        # only add a dir to the stack if its non empty
        # combine the stack at the end

        st = []
        i = 0

        while i < len(path):
            if path[i] == '/':
                i+=1
                direc = ""
                while i < len(path) and path[i] != '/':
                    direc+=path[i]
                    i+=1
                if len(direc) == 0 or direc == ".":
                    continue
                elif direc == "..":
                    if st:
                        st.pop()
                else:
                    st.append(direc)
            else:
                i+=1

        res = "/"
        res+="/".join(st)

        return res

