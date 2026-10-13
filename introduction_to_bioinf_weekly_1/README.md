# Weekly Assignment 1: Comparing Organisms by Taxonomy

In this assignment, we will use biological taxonomy to compare pairs of organisms.Taxonomy organizes organisms into a hierarchy of groups such as domain, kingdom, phylum, class, order, family, genus, and species. For example, humans and red foxes both belong to the class `Mammalia`, but they belong to different orders: humans to `Primates` and red foxes to `Carnivora`.

In this assignment, you will work with taxonomic data retrieved from the NCBI Taxonomy database. The supplied program already contains the code for accessing NCBI and preparing the taxonomic lineages of several organisms.

Your task is to complete the function `first_differing_major_rank` in `taxonomy.py`.

The function should determine the first major taxonomic rank at which two organisms differ and return:

```python
(rank, taxon_a, taxon_b)
```

For example, a human and a red fox first differ at the rank `order`:

```python
("order", "Primates", "Carnivora")
```

Only modify the part of `taxonomy.py` marked with:

```python
# YOUR CODE HERE
```

A set of unit tests is provided. Your solution is correct when all tests pass.

Run the tests with:

```bash
python -m unittest
```
