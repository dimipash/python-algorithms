class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

class AhoCorasick:
    def __init__(self, keywords):
        self.root = TrieNode()
        self.keywords = keywords
        self.build_trie()
        self.build_fail_links()

    def build_trie(self):
        for keyword in self.keywords:
            node = self.root
            for char in keyword:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.output.append(keyword)

    def build_fail_links(self):
        queue = []
        for char, child in self.root.children.items():
            child.fail = self.root
            queue.append(child)

        while queue:
            current_node = queue.pop(0)
            for char, child in current_node.children.items():
                queue.append(child)
                fail_node = current_node.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail
                child.fail = fail_node.children[char] if fail_node else self.root
                child.output.extend(child.fail.output)

    def search(self, text):
        results = []
        node = self.root
        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.fail
            if not node:
                node = self.root
                continue
            node = node.children[char]
            for keyword in node.output:
                results.append((i - len(keyword) + 1, keyword))
        return results

# Example usage:
if __name__ == "__main__":
    keywords = ["he", "she", "his", "hers"]
    text = "ahishers"
    ac = AhoCorasick(keywords)
    matches = ac.search(text)
    print("Matches found:")
    for start, keyword in matches:
        print(f"Keyword '{keyword}' found at index {start}")
