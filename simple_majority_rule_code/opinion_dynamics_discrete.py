import numpy as np


def set_opinion(G , p_r, p_b=None):
    """
    There a two possible choices of opinion 0 or 1.
    This function set the opinion value for each node following a binomial distribution, each group has a 
    probability value of having opinion 1 equal to p_r red group and p_b blue group.
    In case p_b is not defined we have antisymmetrical probabilites I.E. p_b = 1 - p_r
    
    Parameters:
    ------------
    G : Graph
    
    p_r: Float [0,1]
        Probability of obtaining 1, in the binomial probability of opinion, red group
        
    p_b: Float [0,1]
        Probability of obtaining 1, in the binomial probability of opinion, blue group
    """
    if p_b==None:   #If p_b is not given, we have antisymetrical opinions
        p_b = 1-p_r
    node_list = list(G.nodes('color'))
    for i in node_list:
        if i[1] == 'red':
            G.nodes[i[0]]['opinion'] = np.random.binomial(1,p_r)

        if i[1] == 'blue':
            G.nodes[i[0]]['opinion'] = np.random.binomial(1,p_b)

    return G

def without_external_influence(G,t,all_data=False) :   
    """
    
    """
    vec_sum = []
    vec_sum.append([])
    for i in range(len(G.nodes)):
       
        vec_sum[0].append([G.nodes[i]['color'],G.nodes[i]['opinion']])
    for k in range(t):
        vec_sum.append([])
        for i in range(len(G.nodes)):
            i_edges = list(G.edges(i))
            i_sum = []
            for j in i_edges:
                i_sum.append(G.nodes[j[1]]['opinion'])
            i_sum.append(G.nodes[i]['opinion'])
            if np.mean(i_sum)>0.5:
                i_sum = 1
            if np.mean(i_sum)<0.5:
                i_sum = 0
            if np.mean(i_sum)==0.5:
                i_sum = (np.random.binomial(1,0.5))
            vec_sum[k+1].append([G.nodes()[i]['color'],i_sum])
            G.nodes[i]['opinion'] = i_sum
    ###Statstics from the opinion
    red_opinion_t = [[] for null in range(t+1)]
    blue_opinion_t =[[] for null in range(t+1)]
    opinion_t =     [[] for null in range(t+1)]
    
    for i in range(len(vec_sum)):    
        for j in range(len(vec_sum[i])):
            
            if vec_sum[i][j][0] == 'red':
                red_opinion_t[i].append(vec_sum[i][j][1])
            if vec_sum[i][j][0] == 'blue':
                blue_opinion_t[i].append(vec_sum[i][j][1])
            opinion_t[i].append(vec_sum[i][j][1])
    
    mean_red = [np.mean(k) for k in red_opinion_t]
    mean_blue= [np.mean(k) for k in blue_opinion_t]
    mean_opinion=[np.mean(k) for k in opinion_t]
    if all_data == False:
        return (mean_red,mean_blue,mean_opinion)
    if all_data == True:
        return (mean_red,mean_blue,mean_opinion,vec_sum)
    
def set_resilient_opinion(G ,resilience, p_r,p_r_res,p_b_res=None, p_b=None):
    """
    There a two possible choices of opinion 0 or 1.
    This function set the opinion value for each node following a binomial distribution, each group has a 
    probability value of having opinion 1 equal to p_r red group and p_b blue group.
    In case p_b is not defined we have antisymmetrical probabilites I.E. p_b = 1 - p_r.
    Also define the resilience that is an attachment to an Idea
    
    Parameters:
    ------------
    G : Graph
    
    p_r: Float [0,1]
        Probability of obtaining 1, in the binomial probability of opinion, red group
        
    p_b: Float [0,1]
        Probability of obtaining 1, in the binomial probability of opinion, blue group
    """
    if p_b==None:
        p_b = p_r
    if p_b_res == None:
        p_b_res = p_r_res
    node_list = list(G.nodes('color'))
    for i in node_list:
        if i[1] == 'red':
            G.nodes[i[0]]['opinion'] = np.random.binomial(1,p_r)
            G.nodes[i[0]]['resilience'] = np.random.binomial(1,p_r_res)
            if G.nodes[i[0]]['resilience'] == 1:
                G.nodes[i[0]]['resilience'] = resilience
            else:
                G.nodes[i[0]]['resilience'] = 0

        if i[1] == 'blue':
            G.nodes[i[0]]['opinion'] = np.random.binomial(1,p_b)
            G.nodes[i[0]]['resilience'] = np.random.binomial(1,p_b_res)
            if G.nodes[i[0]]['resilience'] == 1:
                G.nodes[i[0]]['resilience'] = resilience
            else:
                G.nodes[i[0]]['resilience'] = 0
    return G


def with_resilience(G,t,all_data=False) :   
    """
    
    """
    vec_sum = []
    vec_sum.append([])
    for i in range(len(G.nodes)):
       
        vec_sum[0].append([G.nodes[i]['color'],G.nodes[i]['opinion']])
    for k in range(t):
        vec_sum.append([])
        for i in range(len(G.nodes)):
            i_edges = list(G.edges(i))
            i_sum = []
            for j in i_edges:
                i_sum.append(G.nodes[j[1]]['opinion'])
            i_sum.append(G.nodes[i]['opinion'])
            if np.mean(i_sum)+G.nodes[j[0]]['resiliece']>0.5:
                i_sum = 1
            if np.mean(i_sum)+G.nodes[j[0]]['resiliece']<0.5:
                i_sum = 0
            if np.mean(i_sum)+G.nodes[j[0]]['resiliece']==0.5:
                i_sum = (np.random.binomial(1,0.5))
            vec_sum[k+1].append([G.nodes()[i]['color'],i_sum])
            G.nodes[j[1]]['opinion'] = i_sum
    ###Statstics from the opinion
    red_opinion_t = [[] for null in range(t+1)]
    blue_opinion_t =[[] for null in range(t+1)]
    opinion_t =     [[] for null in range(t+1)]
    
    for i in range(len(vec_sum)):    
        for j in range(len(vec_sum[i])):
            
            if vec_sum[i][j][0] == 'red':
                red_opinion_t[i].append(vec_sum[i][j][1])
            if vec_sum[i][j][0] == 'blue':
                blue_opinion_t[i].append(vec_sum[i][j][1])
            opinion_t[i].append(vec_sum[i][j][1])
    
    mean_red = [np.mean(k) for k in red_opinion_t]
    mean_blue= [np.mean(k) for k in blue_opinion_t]
    mean_opinion=[np.mean(k) for k in opinion_t]
    if all_data == False:
        return (mean_red,mean_blue,mean_opinion)
    if all_data == True:
        return (mean_red,mean_blue,mean_opinion,vec_sum)
    
def external_influence(G,t,influence,all_data=False) :   
    """
    
    """
    vec_sum = []
    vec_sum.append([])
    for i in range(len(G.nodes)):
       
        vec_sum[0].append([G.nodes[i]['color'],G.nodes[i]['opinion']])
    for k in range(t):
        vec_sum.append([])
        for i in range(len(G.nodes)):
            i_edges = list(G.edges(i))
            i_sum = []
            for j in i_edges:
                i_sum.append(G.nodes[j[1]]['opinion'])
            i_sum.append(G.nodes[i]['opinion'])
            if (np.mean(i_sum)+influence)>0.5:
                i_sum = 1
            if (np.mean(i_sum)+influence)<0.5:
                i_sum = 0
            if (np.mean(i_sum)+influence)==0.5:
                i_sum = (np.random.binomial(1,0.5))
            vec_sum[k+1].append([G.nodes()[i]['color'],i_sum])
            G.nodes[j[1]]['opinion'] = i_sum
    ###Statstics from the opinion
    red_opinion_t = [[] for null in range(t+1)]
    blue_opinion_t =[[] for null in range(t+1)]
    opinion_t =     [[] for null in range(t+1)]
    
    for i in range(len(vec_sum)):    
        for j in range(len(vec_sum[i])):
            
            if vec_sum[i][j][0] == 'red':
                red_opinion_t[i].append(vec_sum[i][j][1])
            if vec_sum[i][j][0] == 'blue':
                blue_opinion_t[i].append(vec_sum[i][j][1])
            opinion_t[i].append(vec_sum[i][j][1])
    
    mean_red = [np.mean(k) for k in red_opinion_t]
    mean_blue= [np.mean(k) for k in blue_opinion_t]
    mean_opinion=[np.mean(k) for k in opinion_t]
    if all_data == False:
        return (mean_red,mean_blue,mean_opinion)
    if all_data == True:
        return (mean_red,mean_blue,mean_opinion,vec_sum)

def multiple_runs_without_external_influence(N,m,fraction,similitude,number_of_runs,iterations,p_r,p_b=None):
    import generate_homophilic_graph_symmetric as sym
    if p_b == None:
        p_b = p_r
    multi_mean_red = [ [] for _ in range(number_of_runs)]
    multi_mean_blue= [ [] for _ in range(number_of_runs)]
    multi_mean= [ [] for _ in range(number_of_runs)]
    for i in range(number_of_runs):
        G = sym.homophilic_barabasi_albert_graph(N, m , fraction, similitude)
        G = set_opinion(G,p_r,p_b) #Set the values of opinion to each node
        mean_red, mean_blue, mean_opinion= without_external_influence(G,iterations)  #Temporal dynamics
        multi_mean_red[i].append(mean_red)
        multi_mean_blue[i].append(mean_blue)
        multi_mean[i].append(mean_opinion)
    final_blue = []
    final_red = []
    final_all = []
    for i in range(iterations):
        blue, red, opi_all = [],[],[]
        for j in range(number_of_runs):
            red.append(multi_mean_red[j][0][i])
            blue.append(multi_mean_blue[j][0][i])
            opi_all.append(multi_mean[j][0][i])
        final_blue.append(np.mean(blue))
        final_red.append(np.mean(red))
        final_all.append(np.mean(opi_all))
    
    return final_red, final_blue, final_all