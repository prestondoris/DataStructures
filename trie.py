class TrieNode(object):
    def __init__(self):
        self.charsOfKey = [None]*26
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        # initializes the trie with a new empty TrieNode by calling
        self.root = self.__createNode()

    def __createNode(self):
        return TrieNode()

    def __charConvertToIndex(self, char):
        # This helper function is case insensitive. It will take uppercase and
        # lowercase letters from a string to give a value between 0 and 25 to
        # be used as the indecies for TrieNode

        if 65 <= ord(char) <= 90:
            return ord(char) - 65
        elif 97 <= ord(char) <= 122:
            return ord(char) - 97

    def insert(self, key):
        cur = self.root

        for char in key:
            index = self.__charConvertToIndex(char)

            if not cur.charsOfKey[index]:
                cur.charsOfKey[index] = self.__createNode()
            cur = cur.charsOfKey[index]

        cur.endOfWord = True

    def search(self, key):
        cur = self.root

        for char in key:
            index = self.__charConvertToIndex(char)
            if not cur.charsOfKey[index]:
                return False
            cur = cur.charsOfKey[index]

        if cur.endOfWord == True:
            return True
        else:
            return False


trie = Trie()
keys = ['Hello', 'world', 'hi', 'there']
for key in keys:
    trie.insert(key)

keys.append('hello')
for key in keys:
    if trie.search(key):
        print '%s is in the Trie' %key
