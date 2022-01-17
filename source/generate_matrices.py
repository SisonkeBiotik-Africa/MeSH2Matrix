# List the MeSH Qualifiers
qualifiers = ["analysis", "blood", "cerebrospinal fluid", "isolation & purification",
              "urine", "anatomy & histology", "blood supply", "cytology", "ultrastructure",
              "embryology", "abnormalities", "innervation", "pathology", "chemistry",
              "agonists", "analogs & derivatives", "antagonists & inhibitors",
              "chemical synthesis", "diagnosis", "diagnostic imaging", "etiology",
              "chemically induced", "complications", "secondary", "congenital",
              "embryology", "genetics", "immunology", "microbiology", "virology",
              "parasitology", "transmission", "organization & administration",
              "economics", "legislation & jurisprudence", "standards",
              "supply & distribution", "trends", "pharmacology", "adminstration & dosage",
              "adverse effects", "poisoning", "toxicity", "agonists",
              "antagonists & inhibitors", "pharmacokinetics", "physiology", "genetics",
              "growth & development", "immunology", "metabolism", "biosynthesis", "blood",
              "cerebrospinal fluid", "deficiency", "enzymology", "pharmacokinetics", "urine",
              "physiopathology", "statistics & numerical data", "epidemiology", "ethnology",
              "mortality", "supply & distribution", "therapeutic use", "administration & dosage",
              "adverse effects", "poisoning", "therapy", "diet therapy", "drug therapy",
              "nursing", "prevention & control", "radiotherapy", "rehabilitation", "surgery",
              "transplantation", "classification", "drug effects", "education", "ethics", "history",
              "injuries", "instrumentation", "methods", "pathogenicity", "psychology", "radiation effects",
              "veterinary"]
with open('output/sample.txt') as f:
    for line in f:
        input01 = line
        if input01 not in ["[]", "['']", "['', '']"]:
            # Getting relation type
            relationtype = input01[:input01.find(";")]
            # Getting the number of considered publications
            input01 = input01[input01.find(";") + 1:]
            NPub = int(input01[:input01.find(";")])
            if NPub > 0:
                # Getting the considered associations
                input01 = input01[input01.find(";") + 1:-1]
                associations = input01[2:-2].split("), (")
                couples = []
                for association in associations:
                    association01 = association
                    association01 = association01[1:-1]
                    associationcouple = association01.split("', '")
                    if len(associationcouple) >= 2:
                        print(associationcouple)
                        if associationcouple[0].find("/") >= 0:
                            subject01 = associationcouple[0].split("/")
                        else:
                            subject01 = [associationcouple[0]]

                        if associationcouple[1].find("/") >= 0:
                            object01 = associationcouple[1].split("/")
                        else:
                            object01 = [associationcouple[1]]
                        for s in subject01:
                            for o in object01:
                                couples.append((s, o))
                # Creating the Matrix for the Associations
                matrix = []
                for q in qualifiers:
                    row = []
                    for r in qualifiers:
                        row.append(round(couples.count((q, r)) / NPub, 3))
                    matrix.append(row)
                with open('output/dataset.txx', "a") as f1:
                    f1.write(str(matrix) + ";" + relationtype + "\n")
