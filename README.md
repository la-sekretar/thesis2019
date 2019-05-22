# thesis2019
This is a repository with the data and analysis for a submitted Biochemistry Part II project work that was done at the University of Cambridge
<ul>
<li>Project name: Careful assessment of the impact of missense mutations on protein stability
<li>Supervisor: Prof Sir Tom Blundell
<li>Day-to-day supervisor: Dr Pedro H. Torres
<li>Duration: 2 months 
</ul>

### Abstract

The current state of the next-generation genomics technologies allows collecting extensive data on
the disease-associated genetic variants. For example, just in association with oncology, almost 6
million coding mutations have been identified to date in the COSMIC database. One of the
challenges for our understanding of the tumour development mechanisms is to characterise
functionally important mutations and separate them from those that have a neglectable effect. As
protein functions rely on the maintenance of the correct folding of its three-dimensional structure
in a given environment, the impact of the mutation on stability (ΔΔG) is considered as an important
parameter. Although it is possible to conduct experimental measurements of ΔΔG values for each
mutation, the existence of such a massive dataset like COSMIC requires the development of
computational tools that could perform automatic high throughput analysis. Many computation
ΔΔG prediction methods have been designed, however, the reports of significant biases, as well as
a relatively low cross-correlation between the models’ predictions, raised questions about the
current value and applicability of these tools. In this work, a comparative analysis of the five
existed ΔΔG prediction tools was made. Then a concept borrowed from computational chemistry,
applicability domain, was used both to improve prediction quality and to investigate dependencies
between structural characteristics of mutations and models prediction.

### Code
Data accumulation and analysis was performed in Python and R languages. The raw mutation data is stored in folder "dataset". The aggregation of the predictions made with individual program (SDM, mCSM, MAESTRO, MUPRO and CUPSAT) is in jupyter notebook <b>"data aggregation"</b>. Analysis steps are mainly split between notebooks <b>"Smart_Data_Analysis"</b> and <b>"Smart_Data_Analysis_3"</b>.
