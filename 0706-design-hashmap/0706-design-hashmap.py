class MyHashMap:

    def __init__(self):
        # Initialize an array of size 1,000,001 with -1
        self.hash_map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Update or insert the value at the given key index
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        # Return the value at the key index (-1 if it doesn't exist)
        return self.hash_map[key]

    def remove(self, key: int) -> None:
        # Reset the value at the key index back to -1
        self.hash_map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)