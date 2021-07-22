from copy import deepcopy


class Node():
    def __init__(self, matrix, childs = []):
        self.matrix = matrix
        self.childs = childs


def check_winner(m):
    if m[0][0] == m[0][1] and m[0][1] == m[0][2]: #1L
        return m[0][0]
    elif m[1][0] == m[1][1] and m[1][1] == m[1][2]: #2L
        return m[1][0]
    elif m[2][0] == m[2][1] and m[2][1] == m[2][2]: #3L
        return m[2][0]
    elif m[0][0] == m[1][0] and m[1][0] == m[2][0]: #1V
        return m[0][0]
    elif m[0][1] == m[1][1] and m[1][1] == m[2][1]: #2V
        return m[0][1]
    elif m[0][2] == m[1][2] and m[1][2] == m[2][2]: #3V
        return m[0][2]
    elif m[0][0] == m[1][1] and m[1][1] == m[2][2]: # 1D 
        return m[0][0]
    elif m[0][2] == m[1][1] and m[1][1] == m[2][0]: # 2D 
        return m[0][2]

    cont = 0
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j] not in ["X", "O"]:
                return False

    return "V"

def print_matrix(matrix):
    for i in range(0,3):
        for j in range(0,3):
            print(matrix[i][j], end=" ")
        print()
    print()

def empty_matrix():
    m = []
    cont = 1
    for i in range(0,3):
        m.append([])
        for j in range(0,3):
            m[i].append(cont)
            cont += 1
    return m

def change_choice(choice):
    if choice == "X":
        return "O"
    return "X"

def fill_matrix(matrix, choice, father):
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j] not in ["X", "O"]:
                k = matrix[i][j]
                matrix[i][j] = choice
                n = Node(matrix)
                father.childs.append(n)
                print_matrix(matrix)

                if not check_winner(matrix):
                    # fill_matrix(deepcopy(matrix), change_choice(choice), n)
                    matrix[i][j] = k
                else:
                    print(check_winner(matrix))
def generate_all_possibilities():
    head = Node(empty_matrix())
    fill_matrix(empty_matrix(), 'X', head)

    return head


if __name__ == '__main__':
    t = generate_all_possibilities()
    # for i in t.childs:
    #     print_matrix(i.matrix)
    #     print()
    #     print()