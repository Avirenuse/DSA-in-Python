# Trie (Prefix Tree) Implementation
# A tree-like data structure used to store a dynamic set or associative array where the keys are usually strings.
# Time Complexity: Insert, Search, startsWith: O(L) where L is length of word
# Space Complexity: O(ALPHABET_SIZE * L * N) where N is number of words

class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes
        self.children = {}
        # Boolean to indicate if this node represents the end of a word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            # If character not found, create a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move down to that child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    words_to_insert = ["apple", "app", "apricot", "banana", "bat"]
    
    for word in words_to_insert:
        trie.insert(word)
        print(f"Inserted: {word}")
        
    print("\n--- Searches ---")
    print("Search 'apple':", trie.search("apple"))      # True
    print("Search 'app':", trie.search("app"))          # True
    print("Search 'appl':", trie.search("appl"))        # False
    
    print("\n--- Prefix Searches ---")
    print("Starts with 'app':", trie.starts_with("app"))  # True
    print("Starts with 'bat':", trie.starts_with("bat"))  # True
    print("Starts with 'cat':", trie.starts_with("cat"))  # False
