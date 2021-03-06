import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
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
        # Reset graph -- nukes everything each time
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i+1}') 

        # # ONE POSSIBLE SOLUTION ⬇️
        # # --> use a set to check if we've added to possible_friendships already
        # possible_friendships = []
        # already_possibly_friends = set() # o(n) space for generating set
        # for user_id in self.users:
        #     for friend_id in self.users:
        #         if user_id == friend_id: continue # don't add a possible friendship with itself <--> no (1,1)
        #         if (user_id, friend_id) in already_possibly_friends: continue # don't add if already possibly friends
        #         possible_friendships.append((user_id, friend_id))
        #         already_possibly_friends.add((friend_id, user_id)) # add tuple of possible friends to prevent duplicates


        # ANOTHER POSSIBLE SOLUTION ⬇️
        # --> don't allow [friend_id] to go places that would allow duplicates
        # --> [friend_id] should never be less than or equal to the [user_id]
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # print(possible_friendships)
        random.shuffle(possible_friendships)
        # print('---')
        # print(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            # ⬆️⬇️ python3 shorthand ⬆️⬇️
            # self.add_friendship(*friendship)



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
