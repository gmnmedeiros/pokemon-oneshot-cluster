# pokemon-oneshot-cluster

## You are playing Pokemon Yellow. You have low HP and you want to know if its safe to try and one-shot your foe. This is the data for you. 🚀 

This repo is a cluster analysis of the 151 original Pokemon classified by speed and HP. Your health is low and you want to see the viability of 'hail-marying' and trying to one-shot your foe. Against which Pokémon you can safely do so?

### The process 🧼

The raw data was cleaned using 'Spyder IDE'

The process was fairly simple, as I only needed to extract the original 151 Pokémon.
The solution was as simple as:

`gen1_df = df[df.Generation == 1]`

However, there were also MegaPokemon, which duplicated the Pokedex # column.

The solution I found was not the most elegant one, but it came through.  It was based on the length of the name:

```gen1_df_no_mega = gen1_df[gen1_df.Name.map(len) < 15]```

#### Once it was done, I exported the CSV file and opened the Jupyter Notebook to explore and plot the data

At first, by looking at the plotted data, I decided to run KMeans with 4 clusters.


Then again I scaled the data and used the WCSS/Elbow method to optimize the number of clusters.
For this WCSS ('Within-cluster Sum of Squares'), the code was:

```
number_clusters = range(1,cl_num)
plt.plot(number_clusters, wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
```



So I decided to run the KMeans model with 3 clusters. The plotted data looks like this:


The end result is shown at the end of the Jupyter code as it follows:

```
If our HP is low, 
should we take a potion or hail mary it?

Cluster 0 is purple
 It represents high speed and low-mid health
   Unsafe for "Hail Mary", and trying to one-shot, depending on your Pokemon.
   Advised: taking potion
   
Cluster 1 is green
   Low-mid health and low-mid speed
   Safest for one-shotting. Hail Mary if your Pokemon can.

Cluster 2 is red
  High health and low speed
  One-shotting is unlikely, unless super-effective + stats boost.
  Advised: taking potion
```
