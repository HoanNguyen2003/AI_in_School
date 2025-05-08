def DFSlimit_(initialState, goal, depth_limit):
    stack = [(initialState, 0)]  # Stack lưu trữ node và độ sâu của nó
    explored = []
    
    while stack:
        state, depth = stack.pop()
        
        if state in explored:
            continue
        
        explored.append(state)
        
        if state == goal:
            return explored
        
        if depth < depth_limit:
            for neighbor in reversed(graph.get(state, [])):  # Duyệt theo thứ tự ngược lại để giống bản đầu
                stack.append((neighbor, depth + 1))
    
    return False

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F', 'G', 'H'],
        'C': ['I', 'J', 'K', 'L'],
        'D': ['M', 'N', 'O', 'P'],
        'E': ['Q'],
        'F': ['R'],
        'G': ['S'],
        'H': ['T'],
        'I': ['U'],
        'J': [],
        'K': [],
        'L': ['V'],
        'M': ['W'], 
        'N': ['X'], 
        'O': ['Y'], 
        'P': ['Z'], 
        'Q': [], 
        'R': [], 
        'S': [], 
        'T': [], 
        'U': [], 
        'V': [],
        'W': [], 
        'X': [], 
        'Y': [], 
        'Z': []
    }
    
    depth_limit = 3  # Giới hạn độ sâu
    result = DFSlimit_('A', 'W', depth_limit)

    
    if result:
        s = 'explored: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print("404 not found")
