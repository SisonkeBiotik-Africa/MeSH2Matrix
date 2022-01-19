import pandas as pd
import json

# second-level metaclass
taxonomic = ["P279", "P31", "P361"]
biomedical_symmetric = ["P769", "P2789", "P2293"]
nonbiomedical_symmetric = ["P129", "P1382", "P1889", "P190", "P2959", "P3179", "P3364",
                           "P3403", "P460", "P461", "P47", "P530"]
biomedical_nonsymmetric = ["P1050", "P1057", "P1060", "P128", "P1349", "P1420", "P1582", "P1605", "P1606", "P171",
                           "P1909", "P1910", "P1916", "P1924", "P1995", "P2175", "P2176", "P2239", "P2597", "P2841",
                           "P2849", "P3094", "P3189", "P3190", "P3261", "P3262", "P3490", "P3491", "P3493", "P3781",
                           "P4545", "P4774", "P4954", "P5131", "P5132", "P5572", "P5642", "P636", "P680", "P681",
                           "P682", "P688", "P689", "P702", "P703", "P7500", "P780", "P8339", "P923", "P924", "P925",
                           "P926", "P927"]
nonbiomedical_nonsymmetric = ["P1001", "P10019", "P101", "P1013", "P1034", "P105", "P1056", "P1071", "P1074", "P111",
                              "P112", "P1142", "P121", "P122", "P1269", "P127", "P131", "P1336", "P1343", "P1344",
                              "P1365", "P1366", "P137", "P1376", "P138", "P140", "P141", "P144", "P1478", "P1479",
                              "P150", "P1535", "P1536", "P1537", "P1542", "P155", "P1552", "P1557", "P156", "P1589",
                              "P159", "P1672", "P17", "P1703", "P172", "P176", "P183", "P1830", "P186", "P1880",
                              "P189", "P205", "P206", "P2079", "P2152", "P2184", "P2238", "P2283", "P2286", "P2289",
                              "P2341", "P2360", "P2414", "P2564", "P2575", "P2578", "P2579", "P2596", "P2633",
                              "P2650", "P2670", "P2737", "P276", "P2821", "P2822", "P2868", "P2975", "P30", "P3075",
                              "P3081", "P3095", "P3113", "P3432", "P3437", "P3438", "P355", "P36", "P360", "P366",
                              "P3712", "P3719", "P376", "P3772", "P3774", "P3776", "P3780", "P3828", "P3842", "P397",
                              "P398", "P4000", "P425", "P427", "P4330", "P452", "P457", "P4584", "P4599", "P4600",
                              "P462", "P463", "P4733", "P4843", "P4934", "P495", "P4988", "P50", "P500", "P501",
                              "P5051", "P509", "P5135", "P5136", "P517", "P527", "P5588", "P5869", "P618", "P641",
                              "P642", "P6440", "P6477", "P6530", "P6532", "P664", "P706", "P710", "P737", "P740",
                              "P749", "P790", "P793", "P797", "P805", "P807", "P8225", "P828", "P840", "P859",
                              "P9072", "P910", "P921", "P928", "P9353", "P937", "P9977"]

# first-level metaclass
# biomedical = biomedical_symmetric + biomedical_nonsymmetric
# nonbiomedical = taxonomic + nonbiomedical_symmetric + nonbiomedical_nonsymmetric
# symmetric = biomedical_symmetric + nonbiomedical_symmetric
# nonsymmetric = biomedical_nonsymmetric + nonbiomedical_nonsymmetric
# nontaxonomic = biomedical_symmetric + nonbiomedical_symmetric + biomedical_nonsymmetric + nonbiomedical_nonsymmetric

all_first_level_classes = [biomedical_symmetric, taxonomic, nonbiomedical_symmetric, taxonomic,
                           nonbiomedical_nonsymmetric]
encoding = pd.read_csv('../output/label_encoded.csv')
labels, encoded_value = encoding.label.tolist(), encoding.encoding.tolist()

second_level_dict = {key: value - 1 for key, value in zip(labels, encoded_value)}
new_first_level = []
for first_level in all_first_level_classes:
    first_level_ = [second_level_dict[element] for element in first_level if element in list(second_level_dict.keys())]
    new_first_level.append(first_level_)

first_level_dict = {index: list_values for index, list_values in enumerate(new_first_level)}

json_object = json.dumps(first_level_dict)

with open("../output/first_level.json", "w") as outfile:
    outfile.write(json_object)
