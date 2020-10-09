from room import Room
from player import Player
from world import World
from utils import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

''' ⬇️ how ⬇️ '''
# ----> ⬇️ recursive_room_map() ⬇️ <-----
#   RETURNS:
#       1. room_exit_dictionary
#       2. visited_nodes_path
#   --> similar to dfs_recursive in [2202-gp/graph.py]
#       --> go from dead-end to dead-end
# ----> ⬇️ bfs() ⬇️ <-----
#   --> find shortest path from node-to-node using visited_node_path
#   --> update the 'n' 's' 'e' 'w' path taken

def recursive_room_search(starting_room, room_graph, room_exit_dictionary=None, visited_nodes_path=None):
    if visited_nodes_path is None:
        visited_nodes_path = []
    if room_exit_dictionary is None:
        room_exit_dictionary = {}
    # capture the [current_room_id] from [starting_room]
    current_room_id = starting_room.id

    if current_room_id not in room_exit_dictionary.keys():
        # mark node (room) as visited <--> add to visited_nodes_path list
        visited_nodes_path.append(current_room_id)
        # add room id entry to room_exit_dictionary
        room_exit_dictionary[current_room_id] = {}
        # get the exits for this room

        possible_exits = starting_room.get_exits()
        # print(current_room_id, possible_exits)

        # for each possible exit direction ...
        #   capture next_room
        #   --> get_room_in_direction()
        #   UPDATE room_exit_dictionary w/ room id
        #   --> update value in current_room key of exit dictionary 
        #   RECURSIVELY call [recursive_room_search(a,b,c,d)]
        #   --> [starting_room] becomes [next_room]
        #   --> [room_exit_dictionary] & [visited_nodes_path] have been updated
        # ⬇️ COMMENT OUT (shuffle) to always get the same answer? ⬇️
        random.shuffle(possible_exits)
        for direction in possible_exits:
            # print(f'direction taken: {direction}')
            next_room = starting_room.get_room_in_direction(direction)
            room_exit_dictionary[current_room_id].update({direction: next_room.id})
            recursive_room_search(next_room, room_graph, room_exit_dictionary, visited_nodes_path)

        if len(room_exit_dictionary) == len(room_graph):
            return room_exit_dictionary, visited_nodes_path

''' ⬇️ bfs ⬇️ '''
#   used to add [direction_path] to [traversal_path] as we step through the [visited_nodes_path] and map the directions
def bfs(starting_room, next_room, room_exit_dictionary):
    # [visited_nodes_path] allows us to run faster without visiting/updating room multiple times
    visited_nodes_path = set()
    room_queue = Queue() # queue to explore room order
    direction_path_queue = Queue() # queue the exit directions travel
    
    room_queue.enqueue([starting_room]) # queue start at starting room
    direction_path_queue.enqueue([]) # blank bc we have not moved yet
    
    while room_queue.size() > 0:
        
        next_path = room_queue.dequeue() # capture next path to explore from room queue
        
        direction_path = direction_path_queue.dequeue() # capture next direction to travel
        
        # last room in next_path taken from queue <--> newest explored room
        last_room_in_next_path = next_path[-1] 
        # if the last room in the next path has not been visited ...
        # --> add that room to the [visited_nodes_path]
        if last_room_in_next_path not in visited_nodes_path:
            visited_nodes_path.add(last_room_in_next_path)
            # if that new room is the next_room we're looking for ...
            # --> return the [direction_path] to be added to the [traversal_path]
            if last_room_in_next_path == next_room:
                # print(direction_path)
                return direction_path
            # if not, 
            # --> keep going in all directions this room has possible exits for
            # HOW?
            # --> make a copy of both next_path + direction_path
            # --> append new room exits + directions to the copies
            # --> enqueue copies to room + directions path queues
            for direction in room_exit_dictionary[last_room_in_next_path]:
                # copy both queues
                path_copy = next_path.copy()
                dirpath_copy = direction_path.copy()
                # adding the newest room and direction to the copied room_path route 
                path_copy.append(room_exit_dictionary[last_room_in_next_path][direction])
                dirpath_copy.append(direction)
                room_queue.enqueue(path_copy)
                direction_path_queue.enqueue(dirpath_copy)


''' ⬇️ traversal_path ⬇️ '''
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# place the player in starting room
# player = Player(world.starting_room)

# use recursive function to visit all rooms and create a [room_exit_dictionary]
room_exit_dictionary, visited_nodes_path = recursive_room_search(world.starting_room, room_graph)
# print(visited_nodes_path)
for i in range(len(visited_nodes_path) - 1):
    # find the path from room to room using visited_nodes_path
    path = bfs(visited_nodes_path[i], visited_nodes_path[i + 1], room_exit_dictionary)
    # print(f'path from {visited_nodes_path[i]} to {visited_nodes_path[i+1]}: {path}')
    traversal_path.extend(path)
# print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
