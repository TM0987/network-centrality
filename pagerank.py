import numpy as np

def wd_pagerank(graph, theta, gamma):

    threshold = 0.000000000000001
    
    unweighted_graph = np.where(graph > 0, 1, 0)

    s_out = []
    for j in range(len(graph)):
        s_out.append(np.sum(graph[:,j]))


    d_out = []
    for j in range(len(unweighted_graph)):
        d_out.append(np.sum(unweighted_graph[:,j]))


    weighted_probablity_matrix = graph
    unweighted_probablity_matrix = unweighted_graph
    for j in range(len(graph)):
        weighted_probablity_matrix[:,j] = weighted_probablity_matrix[:,j] / s_out[j]
        unweighted_probablity_matrix[:,j] = unweighted_probablity_matrix[:,j] / d_out[j]


    M = (theta * weighted_probablity_matrix) + ((1 - theta) * unweighted_probablity_matrix)
    uniformR = (1 - gamma) / len(graph)

    r=(1.0+np.zeros([len(M), 1]))/len(M)
    r_prev = r

    
    for i in range(1,1000):

        r = gamma * np.matmul(M, r_prev) + uniformR

        diff = np.sum(abs(r-r_prev))

        if (diff < threshold):
            break

        r_prev = r

    return {str(index): value[0] for index, value in enumerate(r)}



    

    