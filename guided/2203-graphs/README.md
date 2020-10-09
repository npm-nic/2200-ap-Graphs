# Graphs III

- recorded lecture [here](https://www.youtube.com/watch?v=2bYteFxobwM&feature=youtu.be)

---

## Island Notes

"unconnected" components are still connected...to themselves!!

- they are an "island"

❓ How do we count how many separate "islands" in a graph ❓

- see `islands.py`
- we do things in 2 passes
  - search for every `1` node
    - when we find one, switch gears and `bft()` and mark each as visited

---

## Random Graph Notes

- this should help with the random social network afternoon project [here](../../projects/social/README.md)
- `populate_graph.py` from Beej [here](populate_graph.py)
