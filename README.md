# Opinion_Dynamics_Models_Homophilic_Networks
Models of opinion dynamics in homophilic networks.

Generating symmetric homophilic graphs using the script generate_homophilic_graph_symmetric in https://github.com/frbkrm/NtwPerceptionBias.
Measure mean opinions when used two groups with the same fraction of nodes, in function of similitude, to multiple models,
Already implemented:
  Voter model like
 To be implemented:
  Classic voter model(With and without external influence)
  
 Those were the more interesting results using the majority rule.
The homophilic networks have 2 groups a "Red" and a "Blue" group, the similitude parameter work to determine how probable is a node to attach for a node of the same
group, this parameter will go from [0,1], the higher the value of similitude the more probable is a link between nodes of the same group.
More details in F. Karimi, M. Génois, C. Wagner, P. Singer, and M. Strohmaier, “Homophily influences ranking of minorities in social networks,” Scientific reports, vol. 8, no. 1, pp. 1–12, 2018.
For the networks parameters I used that the red group will be 50% of the nodes and the blue group also 50%. I also used the numbers of how many connections
each node can make, I do not put the results in here because the number of connections did not affect the results.

For the opinion dynamics I assumed that each node can have an opinion equal to 0 or 1. Each blue node will have a probability p_b of having an opinion equal to 1, 
and Red nodes p_r. At each time step all the nodes will update their opinion, to do this is assume that the opinion will be decide by an majority rule,
in case the mean of the sum of neighbors is equal to 0.5, will be rolled another opinion with probability 0.5 of having an opinion equal to 1.

To obtain the results 200 simulations of the model was done and I waited until the 20th iteration to obtain the final opinion, in my simulations I observed that this
system reached to the equilibrium in a maximum of 8 iterations, so it is really observed the final estate of the system.

This is the most representative results


![Difference2_prob_x_similitude_m=3](https://user-images.githubusercontent.com/64976563/102395758-548e2200-3fba-11eb-9e72-7a5ab304a309.png)


