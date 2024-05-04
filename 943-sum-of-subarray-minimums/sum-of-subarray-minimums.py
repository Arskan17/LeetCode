class Solution:
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7

        stack = []
        prev = [None] * len(A)

        for i in range(len(A)):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        next_ = [None] * len(A)
        stack = []
        for k in range(len(A) - 1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else len(A)
            stack.append(k)

        return sum((i - prev[i]) * (next_[i] - i) * A[i] for i in range(len(A))) % MOD
