import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:  # makes a class
    def __init__(self):  # constructor
        # attributes
        self.last_id = 0  # automatically increment the ID to assign the new user
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
            """
            Takes a number of users and an average number of friendships
            as arguments
            Creates that number of users and a randomly distributed friendships
            between those users.
            The number of users must be greater than the average number of friendships.
            """
            # Reset graph
            self.last_id = 0
            self.users = {}
            self.friendships = {}

            # !!!! IMPLEMENT ME
            # Add users
            # Use add_user num_users times

            # Create friendships
            for i in range(0, num_users):
                self.add_user(f"User {i+1}")

            # Generate all friendship combinations
            possible_friendships = []
            
            # Avoid dupes by making sure first number is smaller than second
            for user_id in self.users:
                for friend_id in range(user_id+1, self.last_id+1):
                    possible_friendships.append((user_id, friend_id))

            # Shuffle all possible friendships
            random.shuffle(possible_friendships)

            # Create for first X pairs x is total //2
            for i in range(num_users * avg_friendships // 2):
                friendship = possible_friendships[i]
                self.add_friendship(friendship[0], friendship[1])



    def get_all_social_paths(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])

        # Create a set of traversed vertices
        visited = {}

        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            
            # if not visited
            # checks dictionary key
            if not visited.get(path[-1], None):

                # print(path[-1])
                # mark as visited
                visited[path[-1]] = path

                # enqueue all neightbors
                for next_vert in self.friendships[path[-1]]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        # output
        return visited # TODO



    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])

        # Create a set of traversed vertices
        visited = set()

        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        pass  # TODO


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(2)
    print(connections)
