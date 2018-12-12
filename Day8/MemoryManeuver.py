# Adent of code 2018
# --- Day 8: Memory Maneuver ---
# Part One

def parseNode(data):
    childQuantity, metadataQuantity = data[:2]
    childNode = data[2:]
    scores = []
    metasum = 0

    for _ in range(childQuantity):
        total, score, childNode = parseNode(childNode)
        metasum += total
        scores.append(score)

    metasum += sum(childNode[:metadataQuantity])

    if childQuantity == 0:
        return (metasum, sum(childNode[:metadataQuantity]), childNode[metadataQuantity:])

    value = sum(scores[k - 1] for k in childNode[:metadataQuantity] if 0 < k <= len(scores))
    return (metasum, value, childNode[metadataQuantity:])

if __name__ == '__main__':
    data = [int(x) for x in open('day8.txt').read().split()]
    meta, root, _data = parseNode(data)
    print(meta)
print(root)
