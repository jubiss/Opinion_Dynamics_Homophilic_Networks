# Result Majority Rule

The homophilic networks have 2 groups a "Red" and a "Blue" group, the similitude parameter work to determine how probable is a node to attach to a node of the same group, this parameter will go from [0,1], the higher the value of similitude the more probable is a link between nodes of the same group.
More details in F. Karimi, M. Génois, C. Wagner, P. Singer, and M. Strohmaier, “Homophily influences ranking of minorities in social networks,” Scientific reports, vol. 8, no. 1, pp. 1–12, 2018.
For the network parameters, I used that the red group will be 50% of the nodes and the blue group also 50%. I also used the numbers of how many connections
each node can make, I do not put the results in here because the number of connections did not affect the results.

For the opinion dynamics, I assumed that each node can have an opinion equal to 0 or 1. Each blue node will have a probability p_b of having an opinion equal to 1, 
and Red nodes p_r. At each time step all the nodes will update their opinion, to do this is assume that the opinion will be decided by a majority rule,
in case the mean of the sum of neighbors is equal to 0.5, will be rolled another opinion with a 50% probability of having an opinion equal to 1.

To obtain the results 200 simulations of the model were done and I waited until the 20th iteration to obtain the final opinion. In my simulations, I observed that the system reached equilibrium in a maximum of 8 iterations, but I waited until the 20th iteration to be sure that the system is in equilibrium.

## Most representative result

![Difference2_prob_x_similitude_m=3](https://user-images.githubusercontent.com/64976563/102395758-548e2200-3fba-11eb-9e72-7a5ab304a309.png)

It was plotted the similitude value that will be a measure of homophily in the network x p_r-p_b, where p_b and p_r is the initial probability used to set the opinion values
for each node. The color of this heat map is related to the difference in the mean final opinion of each group, when close to zero we have a consensus, and close to 1
we have polarization between both groups.

The interesting part of this model is that polarization can be observed with a simple majority rule, and also we can observe a phase transition like phenomenal.
The plot is only from 0.4 to 0.9 because all values lesser than 0.5 are going to zero or only having small fluctuations, that could be explained because of the number
of simulations.

I also plotted other results like how the mean opinion of the entire network and for each group. Some of them are also interesting, but this certainly is the most interesting.
