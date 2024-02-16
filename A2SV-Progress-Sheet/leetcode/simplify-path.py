class Solution:
    def simplifyPath(self, path: str) -> str:
        all_dir = path.split("/")
        stack = []
        for d in all_dir:
            if d:
                if d == ".":
                    continue
                if d == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(d)
  
        return "/" + "/".join(stack)