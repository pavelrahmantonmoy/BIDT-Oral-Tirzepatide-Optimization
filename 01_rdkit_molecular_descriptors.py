"""
Biologically Informed Digital Twin (BIDT) - Module 01
Molecular Descriptor Computation and Topological Complementarity Analysis
Author: Pavel Rahman Tonmoy
"""

import sys
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs, Descriptors


def compute_molecular_descriptors(smiles_str, molecule_name):
    mol = Chem.MolFromSmiles(smiles_str)
    if mol is None:
        raise ValueError(f"Invalid SMILES string for {molecule_name}")

    mol_h = Chem.AddHs(mol)

    descriptors = {
        "Molecule": molecule_name,
        "MW (g/mol)": round(Descriptors.MolWt(mol), 2),
        "LogP": round(Descriptors.MolLogP(mol), 2),
        "TPSA (A^2)": round(Descriptors.TPSA(mol), 2),
        "H-Bond Donors": Descriptors.NumHDonors(mol),
        "H-Bond Acceptors": Descriptors.NumHAcceptors(mol),
        "Rotatable Bonds": Descriptors.NumRotatableBonds(mol),
    }
    return mol, descriptors


def compute_tanimoto_similarity(mol1, mol2):
    fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, radius=2, nBits=2048)
    fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, radius=2, nBits=2048)
    similarity = DataStructs.TanimotoSimilarity(fp1, fp2)
    return round(similarity, 4)


if __name__ == "__main__":
    snac_smiles = "O=C(O)CCCCCCCNC(=O)C1=CC=CC=C1O"

    print("=" * 60)
    print("BIDT MOLECULAR DESCRIPTOR CALCULATION")
    print("=" * 60)

    mol_snac, snac_desc = compute_molecular_descriptors(
        snac_smiles, "SNAC (Permeation Enhancer)"
    )
    for key, val in snac_desc.items():
        print(f"{key:20s}: {val}")

    print("-" * 60)
    print("Cheminformatics processing completed successfully.")
