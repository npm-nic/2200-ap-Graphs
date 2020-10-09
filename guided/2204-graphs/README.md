# Graphs-IV

- recorded lecture [here](https://www.youtube.com/watch?v=iB2Mza1mzjo&feature=youtu.be)

---

## Social

- see root/projects/social/[social.py](../../projects/social/social.py)
- worked on `populate_graph()`

Fisher-Yates Shuffle

> "Really Cool" -- Beej

- O(n)
- see [wiki](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)

This gets kind of slow when you have a lot of people

- we are looping through _every_ possible combination for _every_ person
- this first approach is okay but Beej has something better in mind

Second Approach [here](../../projects/social/social2.py)

- really good for big lists with small average friends
- gets worse as average # of friends increases
- WHY?
  - if 74/100 users have already been chosen, you will have a _ton_ of collisions looking for those last few available possible friends

❓ Where is that cross-over point❓

- Beej's `social.py` notes today [here](social.py)
