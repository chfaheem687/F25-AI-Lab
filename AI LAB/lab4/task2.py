from search_core import G, H, astar
for label, h in [("A*", H), ("UCS", {node: 0 for node in H})]:
    cost, path, processed, expanded = astar(G, h)
    independent = sum(next(weight for nxt, weight in G[u] if nxt == v)
                      for u, v in zip(path, path[1:]))
    print(label, "path:", path, "cost:", cost, "checked cost:", independent)
    print("processed:", processed, "expanded:", expanded, "count:", len(expanded))
