"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
def generate_valid_parenthesis(n):
    result = []

    def backtrack(current_string,open_count,close_count):
        if len(current_string) == 2 * n:
            result.append(current_string)
            return
        if open_count < n:
            backtrack(current_string + "(", open_count+1,close_count)

        if close_count<open_count:
            backtrack(current_string+")",open_count,close_count+1)

    backtrack("",0,0)
    return result


print(generate_valid_parenthesis(n=3))