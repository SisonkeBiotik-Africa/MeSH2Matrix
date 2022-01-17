# Extraction of MeSH qualifiers Associations in PubMed
from Bio import Entrez, Medline
import os

Entrez.email = 'turkiabdelwaheb@hotmail.fr'

with open('output/rellist.tsv') as f:
    data = f.readlines()
data = [word.replace("\n", "") for word in data]
# Getting the MeSH ID of the subject and object as well as the Wikidata relation type
for rel in data:
    relation = rel.split("\t")
    relation[1] = relation[1].replace("http://www.wikidata.org/prop/direct/", "")
    relation[0] = str(ord(relation[0][0])) + relation[0][1:]
    relation[2] = str(ord(relation[2][0])) + relation[2][1:]
    # Getting the name of the Subject in MeSH
    handle = Entrez.esummary(db="mesh", id=relation[0], retmode="xml")
    records = Entrez.parse(handle)
    try:
        for record in records:
            subj = record['DS_MeshTerms'][0]
        handle.close()
        # Getting the name of the Object in MeSH
        handle = Entrez.esummary(db="mesh", id=relation[2], retmode="xml")
        records = Entrez.parse(handle)
        for record in records:
            obj = record['DS_MeshTerms'][0]
        handle.close()
        # Formulating the PubMed Query
        query = '("' + subj + '"[Mesh]) AND "' + obj + '"[Mesh]'
        print(query)
        # Searching for the PubMed records having the Subject and Object as MeSH Terms
        handle = Entrez.esearch(db="pubmed", retmax=100, term=query, sort="relevance")
        records1 = Entrez.read(handle)
        handle.close()
        NPub = int(records1["Count"])
        PubIds = records1["IdList"]
        if NPub > 100: NPub = 100
        Associations = []
        for publication in PubIds:
            handle = Entrez.efetch(db="pubmed", id=publication, rettype="medline", retmode="text")
            records2 = Medline.parse(handle)
            for r in records2:
                MeSHTerms = r.get("MH", "?")
            # Extracting the Subject-Object Qualifiers Associations in MeSH Terms
            Subjs = [item.replace("*", "") for item in MeSHTerms if (item.find(subj) >= 0) and (item.find("/") >= 0)]
            Objs = [item.replace("*", "") for item in MeSHTerms if (item.find(obj) >= 0) and (item.find("/") >= 0)]
            for subject1 in Subjs:
                for object1 in Objs:
                    Associations.append((subject1[subject1.find("/") + 1:], object1[object1.find("/") + 1:]))
        # Adding associations to files
        with open('output/sample.txt', 'a') as f1:
            f1.write(relation[1] + ";" + str(NPub) + ";" + str(Associations) + "\n")
        os.system("cls")
    except:
        print('Paper summary failed')
