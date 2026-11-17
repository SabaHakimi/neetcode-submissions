class Node:
    
    def __init__(self, key: int, val: int, prev: Optional[Node] = None, next: Optional[Node] = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1) # Head of LL to track LRU element
        self.head.prev = self.head
        self.head.next = self.head
        
        self.cache = {}      # key -> node; node holds actual val

        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.cache:
            # move accessed node to end
            node = self.cache[key]
            # remove existing entry from LL
            node.prev.next = node.next
            node.next.prev = node.prev

            # add node to end of LL
            node.prev = self.head.prev
            node.next = self.head

            self.head.prev.next = node
            self.head.prev = node

            # return node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update node val
            node = self.cache[key]
            node.val = value

            # remove existing entry from LL
            node.prev.next = node.next
            node.next.prev = node.prev

            # add node to end of LL
            node.prev = self.head.prev
            node.next = self.head

            self.head.prev.next = node
            self.head.prev = node
        else:
            if len(self.cache) == self.capacity:
                # get LRU
                lru = self.head.next

                # remove from cache
                del self.cache[lru.key] 

                # remove LRU from LL
                self.head.next = lru.next
                lru.next.prev = self.head
                
            # create node
            node = Node(key, value, self.head.prev, self.head)

            # add to cache
            self.cache[key] = node

            # add node to end of LL
            self.head.prev.next = node
            self.head.prev = node





                





        
# key struggle is tracking least recently used key
# cache can just be hash table
# need an ordered ds that can add/remove elements O(1) at end and beginning
# doubly linked list with sentinel

# for get simply retrieve if exists
# for put:
# if key exists update cache entry, remove existing entry from list and add to end
# if not exists:
#   if not at capacity just add element to end of list and to cache
#   if at capacity remove least recently used element from cache and from linked list (start of list)
#       then add new element at end of list

# ex
# a d c b a b
# head <-> head
# head <-> a