import generate_homophilic_graph_symmetric as sym
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import opinion_dynamics_discrete as opin_dis
import seaborn as sns
    


########## Seting opinion values  #############################
"""Red is the group with cultural accepted privileges
mean opinion->1 privilege is not recognized and protected
mean opinion->-1 privilege is recognized and attacked"""

number_of_runs = 200
iterations = 20
N, m, minority_fraction = 100, 2, 0.5

"""
Heatmap plots0

"""
similitude = [0.1,0.3,0.5,0.7,0.9]
p_r = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p_b = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
red_data = np.zeros((len(p_r),len(p_b)))
blue_data = np.zeros((len(p_r),len(p_b)))
all_data = np.zeros((len(p_r),len(p_b)))
difference_data = np.zeros((len(p_r),len(p_b)))
diff_simi_data = np.zeros((len(p_r),len(similitude)))
"""
for i in range(len(similitude)):
    for j in range(len(p_r)):
        for k in range(len(p_b)):           
            red, blue, geral = opin_dis.multiple_runs_without_external_influence(N,m,minority_fraction,similitude[i],number_of_runs,iterations,p_r[j],p_b[k])
            red_data[j][k] = red[-1]
            blue_data[j][k] = blue[-1]
            all_data[j][k] = geral[-1]
            difference_data[j][k] = np.abs(red_data[j][k] - blue_data[j][k])
    
    sns.heatmap(red_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_r,yticklabels=p_b)
    plt.xlabel('Probability Red')
    plt.ylabel('Probability Blue')
    plt.title('Red group mean opinion, similitude = ' +str(similitude[i]))
    plt.show()
    
    sns.heatmap(blue_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b)
    plt.xlabel('Probability Red')
    plt.ylabel('Probability Blue')
    plt.title('Blue group mean opinion, similitude = ' +str(similitude[i]))
    plt.show()
    
    sns.heatmap(all_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b)
    plt.xlabel('Probability Red')
    plt.ylabel('Probability Blue')
    plt.title('Mean opinion, similitude = ' +str(similitude[i]))
    plt.show()

    sns.heatmap(difference_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in pinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b\
                ,annot=True,fmt='.2f')
    plt.xlabel('Probability Red')
    plt.ylabel('Probability Blue')
    plt.title('Difference in opinions, similitude = ' +str(similitude[i]))
    plt.show()

    sns.heatmap(difference_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b\
                ,annot=False)
    plt.xlabel('Probability Red')
    plt.ylabel('Probability Blue')
    plt.title('Difference in opinions, similitude = ' +str(similitude[i]))
    plt.show()
    
    diag = [difference_data.diagonal(u) for u in range(len(p_r))]
    diag_mean = [np.mean(u) for u in diag]
    
    for l in range(len(p_r)):
        diff_simi_data[l][i] = diag_mean[l]

sns.heatmap(diff_simi_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=similitude,yticklabels=p_b\
            ,annot=True,fmt='.2f')
plt.xlabel('Similitude')
plt.ylabel('Probability red-blue')
plt.title('Difference in opinions vs similitude')
plt.show()

sns.heatmap(diff_simi_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=similitude,yticklabels=p_b)
plt.xlabel('Similitude')
plt.ylabel('Probability red-blue')
plt.title('Difference in opinions vs similitude')
plt.show()
"""
#HEATMAP CHANGING m
similitude = [0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9]
#m = [5,10,20]
m=[3]
p_r = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
p_b = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

red_data = np.zeros((len(p_r),len(p_b)))
blue_data = np.zeros((len(p_r),len(p_b)))
all_data = np.zeros((len(p_r),len(p_b)))
difference_data = np.zeros((len(p_r),len(p_b)))
diff_simi_data = np.zeros((len(p_r),len(similitude)))

for i in range(len(m)):
    for i2 in range(len(similitude)): 
        for j in range(len(p_r)):
            for k in range(len(p_b)):           
                red, blue, geral = opin_dis.multiple_runs_without_external_influence(N,m[i],minority_fraction,similitude[i2],number_of_runs,iterations,p_r[j],p_b[k])
                red_data[j][k] = red[-1]
                blue_data[j][k] = blue[-1]
                all_data[j][k] = geral[-1]
                difference_data[j][k] = np.abs(red_data[j][k] - blue_data[j][k])
        """
        sns.heatmap(red_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_r,yticklabels=p_b)
        plt.xlabel('Probability Red')
        plt.ylabel('Probability Blue')
        plt.title('Red group mean opinion, similitude=' +str(similitude[i2]) +' m='+str(m[i]))
        plt.show()
        
        sns.heatmap(blue_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b)
        plt.xlabel('Probability Red')
        plt.ylabel('Probability Blue')
        plt.title('Blue group mean opinion, similitude=' +str(similitude[i2])+' m='+str(m[i]))
        plt.show()
        
        sns.heatmap(all_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b)
        plt.xlabel('Probability Red')
        plt.ylabel('Probability Blue')
        plt.title('Mean opinion, similitude=' +str(similitude[i2])+' m='+str(m[i]))
        plt.show()
        """
        sns.heatmap(difference_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in pinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b\
                    ,annot=True,fmt='.2f')
        plt.xlabel('Probability Red')
        plt.ylabel('Probability Blue')
        plt.title('Difference in opinion, similitude=' +str(similitude[i2])+' m='+str(m[i]))
        plt.show()
    
        sns.heatmap(difference_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=p_b,yticklabels=p_b\
                    ,annot=False)
        plt.xlabel('Probability Red')
        plt.ylabel('Probability Blue')
        plt.title('Difference in opinion, similitude=' +str(similitude[i2])+' m='+str(m[i]))
        plt.show()
        
        diag = [difference_data.diagonal(u) for u in range(len(p_r))]
        diag_mean = [np.mean(u) for u in diag]
        
        for l in range(len(p_r)):
            diff_simi_data[l][i2] = diag_mean[l]
    
    sns.heatmap(diff_simi_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=similitude,yticklabels=p_b\
                ,annot=True,fmt='.2f')
    plt.xlabel('Similitude')
    plt.ylabel('Probability red-blue')
    plt.title('Difference in opinions x similitud, m='+str(m[i]))
    plt.show()
    
    sns.heatmap(diff_simi_data,cbar_kws={'ticks':[0.0,0.2,0.4,0.6,0.8,1.0],'label':'Difference in opinion after 20 iterations'},vmin=0,vmax=1,xticklabels=similitude,yticklabels=p_b)
    plt.xlabel('Similitude')
    plt.ylabel('Probability red-blue')
    plt.title('Difference in opinions x similitud, m='+str(m[i]))
    plt.show()


"""
Heatmap plots

"""

"""Opinion trajectory plot"""
"""
similitude = [0.1,0.3,0.5,0.7,0.9]
p = [0,0.25]
for i in range(len(similitude)):

    red, blue, geral = opin_dis.multiple_runs_without_external_influence_0(N,m,minority_fraction,similitude[i],number_of_runs,iterations,p[0])
    
    
    X = range(iterations)
    p1, =plt.plot(X,red,label ='red p='+str(p[0]))
    p2, =plt.plot(X,blue,label = 'blue p=' + str(p[0]))
    #p3, =plt.plot(X,geral,label ='geral p='+str(p[j]))

    red, blue, geral = opin_dis.multiple_runs_without_external_influence_0(N,m,minority_fraction,similitude[i],number_of_runs,iterations,p[1])    
    
    p3, =plt.plot(X,red,label ='red p='+str(p[1]))
    p4, =plt.plot(X,blue,label = 'blue p=' + str(p[1]))
    #p3, =plt.plot(X,geral,label ='geral p='+str(p[j]))
    plt.legend(handles=[p1, p2, p3, p4], title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.title('similitude = ' +str(similitude[i])+'with '+str(number_of_runs)+' simulations')
    plt.show()
"""
"""Opinion trajectory plot"""
