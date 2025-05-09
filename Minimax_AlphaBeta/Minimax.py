from TreeNode import Tree
    
def MaxValue(node):
    if len(node.children) == 0:
        return node
    node.value = -100000
    for child in node.children:
        temp = MinValue(child)
        if temp.value > node.value:
            node.value = temp.value
    return node

def MinValue(node):
    if len(node.children) == 0:
        return node
    node.value = 100000
    for child in node.children:
        temp = MaxValue(child)
        if temp.value < node.value:
            node.value = temp.value 
    return node

def Minimax_Search(state):
    MaxValue(state)

def minimax(self, maximizing_player, depth):
    if self.is_winner('O'):
        return 10 - depth
    if self.is_winner('X'):
        return depth - 10
    if '' not in self.board:
        return 0
    if maximizing_player:
        max_eval = float('-inf')
        for move in self.available_moves():
            self.board[move] = 'O'
            eval = self.minimax(False, depth + 1)
            self.board[move] = ''
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('-inf')
        for move in self.available_moves():
            self.board[move] = 'X'
            eval = self.minimax(True, depth + 1)
            self.board[move] = ''
            min_eval = min(min_eval, eval)
        return min_eval



if __name__ == "__main__":
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")

    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)
    C.add_child(G)
    D.add_child(H)
    D.add_child(I)
    E.add_child(J)
    E.add_child(K)
    F.add_child(M)
    F.add_child(N)
    G.add_child(L)
    G.add_child(Z)

    H.value = 2
    I.value = 9
    J.value = 7
    K.value = 4
    M.value = 8
    N.value = 9
    L.value = 3
    Z.value = 5
    Minimax_Search(A)
    print(A.value)

    