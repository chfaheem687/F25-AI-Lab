from search_core import G, H, astar
for label, h in [("Original", H), ("Changed h(C)=10", {**H, "C": 10})]:
    cost, path, processed, expanded = astar(G, h)
    print(label, "path:", path, "cost:", cost, "expanded:", expanded,
          "count:", len(expanded))
print("True remaining cost at C is 3; original h(C)=2, changed h(C)=10.")
