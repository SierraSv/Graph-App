import numpy
import networkx
import matplotlib.pyplot
import math

def main():
    user_input = 0
    m_dic = {}

    while(user_input != 6):

        user_input = input("Would you like to:\n1. Create a new matrix from scratch\n2. Create a matrix by graph type\n3. Create a product of matrices\n4. Plot a matrix\n5. View information about a matrix\n6. Exit\n")
        user_input = int(user_input)

        if (user_input == 1):
            bad_name = True
            while(bad_name):
                name = input("Please enter a name for your matrix (note: names cannot have spaces):\n")
                if(name.count(' ') == 0):
                    bad_name = False
            m_dic[name] = create_matrix()

        elif(user_input == 2):
            print("Select type of matrix:\n1. Empty Graph\n2. Trivial Graph\n3. Path Graph\n4. Cycle Graph\n5. Complete Graph\n6. Cube Graph\n7. Complete Bipartite Graph\n8. Special Cycle Graph")
            user_input = input()
            user_input = int(user_input)
            num_ver_1 = num_ver_2 = 0
            name = "name"
            if (user_input != 2 and user_input != 6 and user_input != 7):
                print("How many vertices?")
                num_ver_1 = int(input())
            elif (user_input == 6):
                print("The number of vertices is equal to 2^n. What would you like n to be?")
                #num_ver_1 = math.pow(2, int(input()))
                num_ver_1 = int(input())
            elif(user_input == 7):
                print("Please enter the number of vertices for both groups, seperated by a comma:")
                num_vers = input()
                num_vers = num_vers.replace(' ', '')
                num_ver_1 = int(num_vers.split(',')[0])
                num_ver_2 = int(num_vers.split(',')[1])
            name = input("Please enter a name for your matrix (note: names cannot have spaces):\n")
            match user_input:
                case '':
                    print("Bad input")
                case 1:
                    matrix = numpy.zeros((num_ver_1, 1))
                    m_dic[name] = matrix
                    print("Your matrix:\n", matrix)
                case 2:
                    matrix = numpy.zeros((1, 1))
                    m_dic[name] = matrix
                    print("Your matrix\n", matrix)
                case 3:
                    matrix = numpy.zeros((num_ver_1, num_ver_1 - 1))
                    matrix[0][0] = 1
                    matrix[num_ver_1 - 1][num_ver_1 - 2] = 1
                    c = 0
                    for r in range(1, num_ver_1 - 1):
                        matrix[r][c] = matrix[r][c+1] = 1
                        c += 1
                    m_dic[name] = matrix
                    print("Your matrix:\n", matrix)
                case 4:
                    matrix = numpy.zeros((num_ver_1, num_ver_1))
                    matrix[0][0] = matrix[0][num_ver_1-1] = 1
                    c = 0
                    for r in range(1, num_ver_1):
                        matrix[r][c] = matrix[r][c+1] = 1
                        c += 1
                    m_dic[name] = matrix
                    print("Your matrix:\n", matrix)
                case 5:
                    matrix = numpy.zeros((num_ver_1, math.comb(num_ver_1, 2)))
                    c = 0
                    for r1 in range(0, num_ver_1):
                        for r2 in range(r1 + 1, num_ver_1):
                            matrix[r1][c] = matrix[r2][c] = 1
                            c += 1
                    m_dic[name] = matrix
                    print("Your matrix:\n", matrix)
                case 6:
                    ver_list = []
                    num_vers = int(math.pow(2, num_ver_1))
                    matrix = numpy.zeros((num_vers, num_ver_1*int(math.pow(2, num_ver_1-1))))
                    form = '{0:0' + str(num_ver_1) + 'b}'
                    for v in range(0, num_vers):
                        ver_list.append(form.format(v))
                    c = 0
                    for i in ver_list:
                        for n in range(0, num_ver_1):
                            if (i[n] == '0'):
                                inti = int(i, 2)
                                intj = inti + int(math.pow(2, ((num_ver_1-1)-n)))
                                print("inti:", inti, "intj:", intj)
                                if(intj < num_vers):
                                    print("i:", inti, "j:", intj)
                                    matrix[inti][c] = matrix[intj][c] = 1
                                    c += 1
                    m_dic[name] = matrix
                    print("Your matrix:\n", matrix)
                    user_input = 0
                case 7:
                    matrix = numpy.zeros((num_ver_1+num_ver_2, num_ver_1*num_ver_2))
                    c = 0
                    for r1 in range(0, num_ver_1):
                        for r2 in range(num_ver_1, num_ver_2+num_ver_1):
                            matrix[r1][c] = matrix[r2][c] = 1
                            c += 1
                    m_dic[name] = matrix
                    print("Your matrix:\n", matrix)
                case 8:
                    print("What edge rule do you want?")
                    edge_pattern = int(input())
                    matrix = numpy.zeros((num_ver_1, num_ver_1))
                    spec = num_ver_1 - edge_pattern
                    c = 0
                    for v in range(0, num_ver_1):
                        if (edge_pattern == 0):
                            matrix[v][c] = 2
                        elif (v+edge_pattern >= num_ver_1):
                            matrix[v][c] = matrix[v - spec][c] = 1
                        else:
                            matrix[v][c] = matrix[v+edge_pattern][c] = 1
                        c += 1
                    m_dic[name] = matrix
                    print("Your matrix:\n", matrix)


        elif(user_input == 3):
            print("Choose 2 matrices, seperated by a comma")
            for m in m_dic.keys():
                print(m)
            names = input("\n")
            names = names.replace(' ', '')
            name1 = (names.split(','))[0]
            name2 = (names.split(','))[1]
            bad_name = True
            while(bad_name):
                name = input("Please enter a name for your matrix (note: names cannot have spaces):\n")
                if(name.count(' ') == 0):
                    bad_name = False
            if (name1 in m_dic and name2 in m_dic):
                m_dic[name] = create_matrix_product(m_dic[name1], m_dic[name2], name)
            else:
                print("Please choose 2 existing matrices")

        elif(int(user_input) == 4):
            print("Please choose a matrix:")
            for m in m_dic.keys():
                print(m)
            name = input("\n")
            if(name in m_dic):
                plot_matrix(m_dic[name])
            else:
                print("That is not a known matrix")

        elif (int(user_input) == 5):
            print("Please choose a matrix:")
            for m in m_dic.keys():
                print(m)
            name = input("\n")
            if(name in m_dic):
                view_matrix_info(m_dic[name])
            else:
                print("That is not a known matrix")

        elif(user_input != 6):
            print("That is not acceptable input")

    print("Bye!")

def create_matrix():
    dims = input("Enter the number of rows and columns, seperated by a comma: ")
    dims_split = (dims.replace(' ', '')).split(',')
    num_rows = int(dims_split[0])
    num_columns = int(dims_split[1])

    print("Input data for the matrix with commas seperating items, semicolons seperating rows, row by row:")
    data = input()

    matrix = numpy.zeros((num_rows, num_columns))

    r = c = 0
    for x in data.split(';'):
        x = x.replace(' ', '')
        for d in x.split(','):
            matrix[r][c] = int(d)
            c += 1
        c = 0
        r += 1

    print("Your matrix:")
    print(matrix)
    return matrix

def create_matrix_product(matrix1, matrix2, new_name):
    num_rows = matrix1.shape[0] * matrix2.shape[0]
    num_columns = 0
    vertices = []
    edges = []
    for i in range(0, matrix1.shape[0]):
        for j in range(0, matrix2.shape[0]):
            vertex = (i, j)
            vertices.append(vertex)
    for i in vertices:
        for j in vertices:
            if (i == j):
                continue
            elif(i[0] == j[0]):
                for c in range(0, matrix2.shape[1]):
                    if (matrix2[i[1]][c] == 1 and matrix2[j[1]][c] == 1):
                        #print("there should be an edge connecting ", i, "and", j)
                        edge1 = i[0]*matrix2.shape[0] + i[1]
                        edge2 = j[0]*matrix2.shape[0] + j[1]
                        #print("detected an edge connecting", edge1, "and", edge2)
                        if (edges.count((edge1, edge2)) == 0 and edges.count((edge2, edge1)) == 0):
                            edges.append((edge1, edge2))
                            num_columns += 1
                        break
            elif(i[1] == j[1]):
                for c in range(0, matrix1.shape[1]):
                    if (matrix1[i[0]][c] == 1 and matrix1[j[0]][c] == 1):
                        #print("There should be an edge connecting", i, "and", j)
                        edge1 = i[0]*matrix2.shape[0] + i[1]
                        edge2 = j[0]*matrix2.shape[0] + j[1]
                        #print("detected an edge connecting", edge1, "and", edge2)
                        if(edges.count((edge1, edge2)) == 0 and edges.count((edge2, edge1)) == 0):
                            edges.append((edge1, edge2))
                            num_columns += 1
                        break
    new_matrix = numpy.zeros((num_rows, num_columns))
    
    c = 0
    for e in edges:
        new_matrix[e[0]][c] = 1
        new_matrix[e[1]][c] = 1
        c += 1

    #r = c = 0
    #for r in range(0, num_rows):
    #    for c in range(0, num_columns):
    #        if new_matrix[r][c] != 1:
    #            new_matrix[r][c] = 0
    
    print(new_matrix)
    return new_matrix

def plot_matrix(matrix):
    num_rows = matrix.shape[0]
    num_columns = matrix.shape[1]

    G = networkx.Graph()
    nodes = numpy.arange(0, num_rows).tolist()

    G.add_nodes_from(nodes)

    edges = []

    for c in range(0, num_columns):
        edge_pair = []
        for r in range(0, num_rows):
            if (matrix[r][c] == 1):
                edge_pair.append(r)
            elif(matrix[r][c] == 2):
                edge_pair = [r, r]
                break
        edges.append(tuple(edge_pair))

    labels = {}

    for r in range(0, num_rows):
        labels[r] = str(r)

    G.add_edges_from(edges)

    networkx.draw_networkx(G, labels=labels)

    matplotlib.pyplot.show()

def view_matrix_info(matrix):
    print("Your matrix has", matrix.shape[0], "vertices and", matrix.shape[1], "edges")

    t_matrix = matrix.dot(matrix.transpose())

    print("The degree of each vertex is:\n")
    for v in range(matrix.shape[0]):
        print("d(", v, ") =", t_matrix[v][v])

    print("Your matrix transposed:")
    print(matrix.transpose())

    print("matrix * transposed matrix")
    print(t_matrix)


if __name__ == "__main__":
    main()