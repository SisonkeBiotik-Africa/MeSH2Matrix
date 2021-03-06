# MeSH2Matrix
A set of Python codes for the generation of biomedical ontologies from the MeSH keywords of the PubMed scholarly publications

# Description of Output Files
  - output/rellist.tsv: list of relations (size of 81k)
  - output/sample.txt: Set of MeSH qualifiers Associations extracted from PubMed
  - output/label_encoded.csv: Encoding for the 195 unique labels

# Description of Sources Files
  - source/extract_mesh.py: code source to create the set of MeSH qualifiers from PubMed
  - source/generate_matrices.py: Generate the dataset for the modeling part. Each line is the tuple (relation_matrix, label) where relation_matrix is a (89, 89) matrix.
    - Current Statistics:
      - Dataset Size and shape: 46469, (46469, 89, 89)
      - Labels: 195 Unique, and 5 Grouped Labels (see details on our paper)
      - Labels Set Shape: (46469,)
  - source/main.py: Download our existing data set and return a tuple of arrays: (train_data, train_labels), (dev_data, dev_labels) and (test_data, test_labels)
    -  Train Set: (33457, 89, 89)
    -  Dev Set: (13012, 89, 89)
    -  Test Set: (9294, 89, 89)
        - All files are file are automatically downloaded if they not not exist already
        - The grouped labels are obtained mergin all first-level relations types to second-level relations. They are also automatically downloaded
    
# Description of Model Files
  - models/NeuralNets/*: contains training and validation source code for deep learning models (Fully Connected, CNNs). Both models are trained with 195 classes and 5 grouped classes
  - models/TradiMlModels: Traditional ML models like SVM.
  - models/get_pretrained_weights.py: Download pretrained weights of neural nets