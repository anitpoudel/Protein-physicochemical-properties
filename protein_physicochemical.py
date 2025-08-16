from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

records = []
for rec in SeqIO.parse("Oryza_sativa_MYB.fasta", "fasta"):
    seq = str(rec.seq).replace("*", "")
    ana = ProteinAnalysis(seq)
    records.append({
        "protein": rec.description,
        "AA_sequence": seq,
        "molecular_weight": ana.molecular_weight(),
        "isoelectric_point": ana.isoelectric_point()
    })

pd.DataFrame(records).to_excel("physicochemical_properties.xlsx", index=False)
print("Saved to physicochemical_properties.xlsx")
