
class DisjointSet:
    parent = {}
    rank = {}
    counter = {}
    def make_set(self, universe):
        for i in universe:
            self.parent[i] = i
            self.rank[i] = 0
            self.counter[i] = 0

    def find(self, k):
        if self.parent[k] != k:
            result = self.find(self.parent[k])
            self.parent[k] = result[0]
            self.counter[k] += result[1]
            return (self.parent[k], self.counter[k])
        else:
            return (self.parent[k],0)
    def union(self, a, b):
        x_c = self.find(a)
        y_c = self.find(b)
        x = x_c[0]
        y = y_c[0]

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.counter[x]+=1
        elif self.rank[x] < self.rank[y]:
            x,y  = y,x
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] = self.rank[x] + 1
        self.counter[y] -= self.counter[x]
        self.counter[x]+=1
    def the_same_gang(self,x,y):
        x = self.find(x)[0]
        y = self.find(y)[0]
        if (x == y):
            print("YES")
        else:
            print("NO")
    def get_number_of_gangs(self,x):
        res = self.find(x);
        print(res[1] + self.counter[res[0]] + 1)

def print_sets(universe, ds):
    print([ds.find(i) for i in universe])


def ans():
    n, m = map(int, input().split())
    universe = [i for i in range(n)]

    ds = DisjointSet()

    ds.make_set(universe)

    for i in range(m):
        input_numbers = list(map(int, input().split()))
        task_type = input_numbers[0]
        if task_type == 1:
            ds.union(input_numbers[1]-1, input_numbers[2]-1)
        elif task_type == 2:
            ds.the_same_gang(input_numbers[1]-1, input_numbers[2]-1)
        elif task_type == 3:
            ds.get_number_of_gangs(input_numbers[1]-1)
ans()