# K-Anonymity

### The Anonymization method
- Anonymization method aims at making the individual record be indistinguishable among a group record by using techniques of generalization and suppression.
- The rapid growth of database, networking and computing technologies, a large amount of personal data can be integrated and
analyzed digitally, leading to an increased use of data mining tools to infer trends and patterns. 
- This has been raised universal concerns
about protecting the privacy of individuals.

#### K-Anonymity
- Turning a dataset into a k-anonymous (and possibly l-diverse or t-close) dataset is a complex problem, and finding the optimal partition into k-anonymous groups is an NP-hard problem. Fortunately, several practical algorithms exists that often produce "good enough" results by employing greedy search techniques.
- In this tutorial we will explore the so-called "Mondrian" algorithm, which uses a greedy search algorithm to partition the original data into smaller and smaller groups (if we plot the resulting partition boundaries in 2D they resemble the pictures by Piet Mondrian, hence the name).
- The algorithm assumes that we have converted all attributes into numerical or categorical values and that we are able to measure the “span” of a given attribute Xi.

#### L-diversity
- l-diversity ensures that each k-anonymous group contains at least l different values of the sensitive attribute.
- Therefore, even if an adversary can identify the group of a person he/she still would not be able to find out the value of that person's sensitive attribute with certainty.
- Problem that might happen in k-anonymity is that all people in a k-anonymous group possess the same value of the sensitive attribute. An adversary who knows that a person is in that k-anonymous group can then still learn the value of the sensitive attribute of that person with absolute certainty. This problem can be fixed by using l-diversity.

#### T-closeness
- t-closeness is a further refinement of l-diversity group based anonymization that is used to preserve privacy in data sets by reducing the granularity of a data representation. 
- This reduction is a trade off that results in some loss of effectiveness of data management or mining algorithms in order to gain some privacy. 
- The t-closeness model extends the l-diversity model by treating the values of an attribute distinctly by taking into account the distribution of data values for that attribute.
- t-closeness demands that the statistical distribution of the sensitive attribute values in each k-anonymous group is "close" to the overall distribution of that attribute in the entire dataset.
