class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        pos = self.n + index
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# Example usage:
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(data)

    print("Segment Tree:", st.tree)
    print("Sum of values in range [1, 3]:", st.query(1, 3))
    st.update(1, 10)
    print("Updated Segment Tree:", st.tree)
    print("Sum of values in range [1, 3] after update:", st.query(1, 3))
