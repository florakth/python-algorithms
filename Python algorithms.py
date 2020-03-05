# Complete the countingValleys function below.
def countingValleys(n, s):
    set = ['U', 'D']
    if n < 2 or n > 10e6:
        return False
   
    for i in s:
        if i not in set:
            return False

    num_valley = 0
    level = 0
    for c in s:
        if c == 'U':
            level += 1
        else:
            if level == 0:
                num_valley += 1
            level -= 1
    return num_valley


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if n < 1 or n > 100:
        return False
    for i in range(n):
        if ar[i] < 0 or ar[i] > 100:
            return False
    c = 0
    dict_sock = {}
    for i in ar:
        if i not in dict_sock:
            dict_sock[i] = 1
        else:
            dict_sock[i] += 1
            
    for ind in dict_sock:
        c += dict_sock[ind]//2

    return c


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    if n < 2 or n > 100:
        return False
    if c[0] != 0 or c[n-1] != 0:
        return False
    for i in c:
        if i != 0 and i != 1:
            return False
    curr = 0
    jump = 0 

    while curr < n-1:
        if curr == n-2:
            curr += 1
        elif c[curr+2] == 0:
            curr += 2
        else:
            curr += 1
        jump += 1

    return jump


# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) <1 or len(s) > 100:
        return False
    if n<1 or n > 10e12:
        return False
    if len(s)==1 and s == 'a':
        return n
    r = n//len(s)
    num = 0
    num_last = 0
    for a in s:
        if a == 'a':
            num += 1
    for b in range(n%len(s)):
        if s[b] == 'a':
            num_last += 1
    return num*r + num_last



class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):

        sorted_dict = sorted(
            self.standings.items(),
            
            key = lambda kv: (-kv[1]['score'],
                              kv[1]['games_played'],),
            reverse=False)
                
        return sorted_dict[rank-1][0]
      
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))


# Binary Search Tree
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if root.value == value:
        return True
    elif root.value < value:
        if root.right == None:
            return False
        else:
            return contains(root.right,value)
    else:
        if root.left == None:
            return False
        else:
            return contains(root.left,value)
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))
