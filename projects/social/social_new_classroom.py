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
        # add other user data
        # birthday
        # 
    def __repr__(self):
        return self.name

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
            return False

        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False

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

    # new version
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

            # new frendship method
            # randomly make friends, keep new, no dupes
            # til we get ot number we need
            # 

            # keep track of freindships and collisions

            target_friendships = num_users * avg_friendships
            total_friendships = 0
            collisions = 0

            while total_friendships < target_friendships:
                user_id = random.randint(1, self.last_id)
                # we need a friend
                friend_id = random.randint(1, self.last_id)

                if self.add_friendship(user_id, friend_id):
                    # issue: how do you increment
                    # since we divided above, shoudl be 1
                    total_friendships += 2
                else:
                    collisions += 1

            print(f"Total collisions: {collisions}")


            # Generate all friendship combinations
            possible_friendships = []
            
            # Avoid dupes by making sure first number is smaller than second
            for user_id in self.users:
                for friend_id in range(user_id+1, self.last_id+1):
                    possible_friendships.append((user_id, friend_id))

            # # Shuffle all possible friendships
            # random.shuffle(possible_friendships)

            # # Create for first X pairs x is total //2
            # for i in range(num_users * avg_friendships // 2):
            #     friendship = possible_friendships[i]
            #     self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths_class(self, user_id):
        # shortest tells us breadth first
        # extended network - traveersal, connected component
        # planning:
        # how are we going to build a graph? we done did that one
        # Start at given user id, do a bft, return path to each friend
        
        # create q
        qq = Queue()
        # enq path
        qq.enqueue([user_id])
        # create visited
        visited = {}  # dict not set

        # add to visited in a loop
        # while q not empty
        while qq.size() > 0:

            # deq 11st path
            path = qq.dequeue()

            vertex = path[-1]

            # if not visisted
            if vertex not in visited:
                # do the thing
                # add path to visited
                # add to visited
                visited[vertex] = path                

                # for each neighbor
                for neighbor in self.friendships[vertex]:
                    # copy path and enq
                    new_path = path.copy()
                    new_path.append(neighbor)
                    qq.enqueue(new_path)

        return visited


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
    target = 2
    ave_number_of_friends = 10

    sg.populate_graph(ave_number_of_friends, target)
    print("sg.friendships", sg.friendships)

    connections = sg.get_all_social_paths(target)
    print("connections", connections)

    connections2 =sg.get_all_social_paths_class(target)
    print("connections2", connections2)

    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])

    print(f"Avg len of social path: {total_social_paths / len(connections)}")

    # hypothesis: average length of connection:
    # 