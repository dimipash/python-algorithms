class State:
    def __init__(self, length=0, link=None):
        self.length = length
        self.link = link
        self.next = {}

class SuffixAutomaton:
    def __init__(self, text):
        self.text = text
        self.last = State()
        self.states = [self.last]

    def add_char(self, c):
        cur = State(length=self.last.length + 1)
        self.states.append(cur)

        p = self.last
        while p is not None and c not in p.next:
            p.next[c] = cur
            p = p.link

        if p is None:
            cur.link = self.states[0]
        else:
            q = p.next[c]
            if p.length + 1 == q.length:
                cur.link = q
            else:
                clone = State(length=p.length + 1, next=q.next, link=q.link)
                self.states.append(clone)
                cur.link = q.link = clone
                while p is not None and p.next[c] == q:
                    p.next[c] = clone
                    p = p.link

        self.last = cur

    def build(self):
        for c in self.text:
            self.add_char(c)

    def display(self):
        for i, state in enumerate(self.states):
            print(f"State {i}: length={state.length}, link={state.link.length if state.link else None}, next={state.next}")

# Example usage:
if __name__ == "__main__":
    text = "ababc"
    sa = SuffixAutomaton(text)
    sa.build()
    sa.display()
