# (user)Problem: We know who is connected with whom in a social network. 
# But for each person, we do not know the shortest paths between them and each person in their (sub) network. 
 
# (product)Solution: for a given target input network member: output a list of their 
# shortest paths of connection to each person in their (private) network in the following form:
# [ {
# target_user : [target_user],
# user_id_A :  [target_user, user_id_B, user_id_R, ..., user_id_A], 
# user_id_B :  [target_user, user_id_A, user_id_E, ..., user_id_B],
# ...etc...
# } ]

# Plan:
# 
# step 1: make a private network (class instantiation) for user_id input (as hub)
# subnetwork of the main network
# 1.1: see who they connect to
# 1.2: see who they connect to
# 1.3: etc.
 
# Step 2:
# 2.1 make a list of people in that network
 
# Step 3:
# 3.1 do a depth first search
# from the target to each member
# printing path


# helper function to make a set of network members
# this make a sub-list just for the private-social-network
# out of the larger whole social network
def get_members_of_private_network(target_user, dict_of_friends, set_of_done = set(), output_dict = dict()):

    #print("target", target_user)

    # Done repeat yourself
    # don't look up same person twice
    # no more new people to search (base case)
    if target_user in set_of_done:

        # here?
        return output_dict
        #pass 

    elif target_user not in set_of_done:
        # add target_user to set of done:
        set_of_done.add(target_user)

        # mask for relative list of friends
        friends_mask = dict_of_friends[target_user]

        # make an entry for those
        # add key=user: value= [their friends] to the output_dict
        output_dict[target_user] = friends_mask

        #print("friends_mask", friends_mask)

        #recursively repeat for each friend down the chain
        for friend in friends_mask:
            print("friend", friend)
            # recursive call!!
            # run the program on those friends
            return get_members_of_private_network(friend, dict_of_friends, set_of_done, output_dict)

    # here?
    return output_dict
    #pass


dict_of_friends = {1: {8, 9, 4}, 2: {5}, 3: {5}, 4: {1}, 5: {2, 3, 6}, 6: {9, 10, 5}, 7: {10}, 8: {1, 9}, 9: {8, 1, 6}, 10: {6, 7}}


get_members_of_private_network(6, dict_of_friends)
