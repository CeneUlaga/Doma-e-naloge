from Bio import Entrez

Entrez.email = "your.email@example.com"


def fetch_taxon(scientific_name):
    """Fetch a taxonomy record from NCBI."""
    handle = Entrez.esearch(
        db="taxonomy",
        term=scientific_name
    )
    record = Entrez.read(handle)

    if not record["IdList"]:
        raise ValueError(f"No taxonomy record found for {scientific_name}")

    tax_id = record["IdList"][0]

    handle = Entrez.efetch(
        db="taxonomy",
        id=tax_id,
        retmode="xml"
    )
    return Entrez.read(handle)[0]


def lineage_with_ranks(taxon):
    """Return the taxonomic lineage with ranks."""
    lineage = [
        (entry["Rank"], entry["ScientificName"])
        for entry in taxon["LineageEx"]
    ]
    lineage.append((taxon["Rank"], taxon["ScientificName"]))
    return lineage


def first_differing_major_rank(lineage_a, lineage_b):
    """Return the first major rank at which two lineages differ."""
    major_ranks = [
        "superkingdom", "kingdom", "phylum", "class",
        "order", "family", "genus", "species"
    ]

    taxa_a = dict(lineage_a)
    taxa_b = dict(lineage_b)

    for rank in major_ranks:
        taxon_a = taxa_a.get(rank)
        taxon_b = taxa_b.get(rank)

        if taxon_a != taxon_b:
            return rank, taxon_a, taxon_b

    return None


def compare(organism_a, organism_b):
    """Compare the taxonomy of two organisms."""
    lineage_a = lineage_with_ranks(fetch_taxon(organism_a))
    lineage_b = lineage_with_ranks(fetch_taxon(organism_b))

    result = first_differing_major_rank(lineage_a, lineage_b)

    if result:
        rank, taxon_a, taxon_b = result
        print(
            f"{organism_a} vs. {organism_b}: "
            f"{rank} ({taxon_a} vs. {taxon_b})"
        )


pairs = [
    ("Homo sapiens", "Vulpes vulpes"),
    ("Homo sapiens", "Pan troglodytes"),
    ("Vulpes vulpes", "Canis lupus"),
    ("Vulpes vulpes", "Felis catus"),
    ("Homo sapiens", "Mus musculus"),
]

if __name__ == "__main__":
    for organism_a, organism_b in pairs:
        compare(organism_a, organism_b)