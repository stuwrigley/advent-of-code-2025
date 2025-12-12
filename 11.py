#!/usr/bin/python3
import time
import networkx as nx

start_time = time.time()

DAY = '11'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

G = nx.DiGraph()  # we're dealing with a directed graph (DiGraph)
for line in lines:
    nodes = line.split()
    for node in nodes[1:]:
        G.add_edge(nodes[0][:-1], node)

# part 1
paths = nx.all_simple_paths(G, source='you', target='out')  # , cutoff=1000)
print("Part 1 answer:", len(list(paths)))
elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("  Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("  Completed in %.1f s" % elapsedTime)

# part 2
if TEST:
    inputFilename = 'data/' + DAY + '_input' + '_test_part2' + '.txt'
    with open(inputFilename) as f:
        lines = [line.rstrip() for line in f]

    G = nx.DiGraph()
    for line in lines:
        nodes = line.split()
        for node in nodes[1:]:
            G.add_edge(nodes[0][:-1], node)


def traverse(device, end, visited, scores):
    if device == end:
        return 1
    if device in visited or device == "out":
        return 0
    if device in scores:
        return scores[device]
    visited.add(device)
    total = sum([traverse(output, end, visited, scores) for output in list(G.successors(device))])
    visited.remove(device)
    scores[device] = total
    return total


a1 = traverse("svr", "fft", set(), {})
a2 = traverse("fft", "dac", set(), {})
a3 = traverse("dac", "out", set(), {})
b1 = traverse("svr", "dac", set(), {})
b2 = traverse("dac", "fft", set(), {})
b3 = traverse("fft", "out", set(), {})

print("Part 2 answer:", a1 * a2 * a3 + b1 * b2 * b3)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("  Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("  Completed in %.1f s" % elapsedTime)
