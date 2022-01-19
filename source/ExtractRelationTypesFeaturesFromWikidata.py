from wikibaseintegrator import wbi_functions

#List all biomedical relations
biorel = ["P9985", "P10193", "P10228", "P10243", "P351", "P486", "P645",
          "P644", "P662", "P681", "P680", "P682", "P684", "P703", "P702",
          "P1349", "P1531", "P1582", "P1911", "P1910", "P1913", "P1912",
          "P1915", "P1914", "P1916", "P1918", "P1929", "P1990", "P2143",
          "P2158", "P2293", "P2410", "P2520", "P2542", "P2548", "P2576",
          "P2597", "P2849", "P2871", "P2870", "P2874", "P3063", "P3094",
          "P3329", "P3331", "P3406", "P3433", "P3487", "P3488", "P3491",
          "P3490", "P3523", "P3636", "P3741", "P3811", "P3870", "P3937",
          "P3951", "P4081", "P4196", "P4269", "P4268", "P4333", "P4355",
          "P4395", "P4394", "P4628", "P4774", "P4777", "P4863", "P4864",
          "P4866", "P4873", "P4875", "P4882", "P4915", "P4914", "P5211",
          "P5215", "P5214", "P5219", "P5230", "P5315", "P5418", "P5572",
          "P6143", "P6680", "P6694", "P6861", "P6982", "P7001", "P7770",
          "P7862", "P8193", "P8194", "P8697", "P8789", "P8872", "P9169",
          "P9272", "P9521", "P9632", "P128", "P171", "P493", "P492",
          "P494", "P557", "P563", "P593", "P592", "P595", "P604", "P637",
          "P636", "P639", "P638", "P653", "P652", "P663", "P665", "P667",
          "P668", "P673", "P672", "P689", "P688", "P696", "P699", "P698",
          "P704", "P715", "P769", "P780", "P923", "P925", "P924", "P927",
          "P926", "P970", "P1050", "P1055", "P1057", "P1060", "P1193",
          "P1199", "P1323", "P1395", "P1461", "P1550", "P1583", "P1603",
          "P1605", "P1604", "P1606", "P1660", "P1677", "P1691", "P1690",
          "P1693", "P1692", "P1694", "P1748", "P1909", "P1917", "P1925",
          "P1924", "P1928", "P1930", "P1995", "P2074", "P2175", "P2176",
          "P2239", "P2240", "P2275", "P2288", "P2329", "P2646", "P2710",
          "P2712", "P2717", "P2718", "P2789", "P2841", "P2840", "P2844",
          "P2854", "P2892", "P2941", "P2944", "P3098", "P3189", "P9341",
          "P9450", "P9635", "P9853", "P10022", "P10095", "P10094", 
          "P10245", "P3190", "P3201", "P3205", "P3261", "P3262", "P3291",
          "P3292", "P3345", "P3355", "P3354", "P3357", "P3356", "P3359",
          "P3358", "P3457", "P3464", "P3471", "P3489", "P3493", "P3492",
          "P3550", "P3637", "P3640", "P3720", "P3781", "P3841", "P3885",
          "P3945", "P3956", "P3982", "P4044", "P4229", "P4233", "P4235",
          "P4236", "P4250", "P4317", "P4338", "P4425", "P4426", "P4545", 
          "P4954", "P5082", "P5131", "P5133", "P5132", "P5134", "P5248", 
          "P5375", "P5376", "P5415", "P5446", "P5458", "P5468", "P5496", 
          "P5843", "P6220", "P6884", "P7173", "P7329", "P7387", "P7500", 
          "P8011", "P8010", "P8026", "P8049", "P8064", "P8071", "P8150", 
          "P8273", "P8339", "P8401", "P8656", "P8824", "P9107", "P9186",
          "P4670", "P5270", "P5329", "P5642", "P5806", "P7830", "P7995",
          "P8170", "P8204", "P9306", "P9340"]
taxrel = ["P31", "P106", "P136", "P279", "P361", "P1399"]

with open("property.txt", "r") as f:
    for line in f:
        property01 = line[:-1]
        #Verify if the Wikidata relation type is symmetric
        symm = wbi_functions.execute_sparql_query("SELECT * WHERE { ?x wdt:"+property01+" ?y. ?y wdt:"+property01+" ?x. } LIMIT 100")
        symmetric = len(symm["results"]["bindings"])
        #Verify if the Wikidata relation type is biomedical
        if property01 in biorel:
            biomedical = "yes"
        else:
            biomedical = "no"
        #Verify the English label of the Wikidata relation type
        label = wbi_functions.execute_sparql_query('SELECT * WHERE { wd:'+property01+' rdfs:label ?label. FILTER(LANG(?label)="en").}')
        for value in label["results"]["bindings"]:
            name = value["label"]["value"]
        #Verify if the Wikidata relation type is taxonomic
        if property01 in taxrel:
            taxonomic = "yes"
        else:
            taxonomic = "no"
        #Add the results of the queries
        with open("result.txt", "a") as f1:
            f1.write(name+";"+taxonomic+";"+str(symmetric)+";"+biomedical+"\n")
        

            


        
