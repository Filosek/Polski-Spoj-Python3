import sys

try:
    tests = int(input())
    for i in range(tests):
        no_participants = int(input())
        participants = list(map(int, input().split()))
        h_score = max(participants)
        results = []
        for j in range(len(participants)):
            if participants[j] == h_score:
                results.append(participants[j])
        for j in range(participants.count(h_score)):
            participants.remove(h_score)
        participants.sort()
        results += participants
        print(*results)
except:
    sys.exit(0)