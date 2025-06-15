#3475
#medium

#Biologists are studying basic patterns in DNA sequences. Write a solution to identify sample_id with the following patterns:

#Sequences that start with ATG (a common start codon)
#Sequences that end with either TAA, TAG, or TGA (stop codons)
#Sequences containing the motif ATAT (a simple repeated pattern)
#Sequences that have at least 3 consecutive G (like GGG or GGGG)
#Return the result table ordered by sample_id in ascending order.

#The result format is in the following example.

#My own solution using python3:

#just follow the instructions exactly - no tricks

import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples["has_start"] = samples["sample_id"]
    samples["has_stop"] = samples["sample_id"]
    samples["has_atat"] = samples["sample_id"]
    samples["has_ggg"] = samples["sample_id"]
    for i, v in enumerate(samples["dna_sequence"]):
        if v.startswith("ATG"):
            samples["has_start"][i] = 1
        else:
            samples["has_start"][i] = 0
        if v.endswith("TAA") or v.endswith("TAG") or v.endswith("TGA"):
            samples["has_stop"][i] = 1
        else:
            samples["has_stop"][i] = 0
        if "ATAT" in v:
            samples["has_atat"][i] = 1
        else:
            samples["has_atat"][i] = 0

        if "GGG" in v or "GGGG" in v:
            samples["has_ggg"][i] = 1
        else:
            samples["has_ggg"][i] = 0
    
    return pd.DataFrame(samples, columns=["sample_id", "dna_sequence", "species", "has_start", "has_stop", "has_atat", "has_ggg"])
