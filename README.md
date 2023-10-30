# MeSH2Matrix
A set of Python codes for the classification of biomedical relations based on the MeSH keywords of PubMed scholarly publications

**To cite the work**:
* Turki, H., Dossou, B. F. P., Emezue, C. C., Hadj Taieb, M. A., Ben Aouicha, M., Ben Aouicha, M., Ben Hassen, H., & Masmoudi, A. (2022). MeSH2Matrix: Machine learning-driven biomedical relation classification based on the MeSH keywords of PubMed scholarly publications. In *Proceedings of the 12th International Workshop on Bibliometric-enhanced Information Retrieval co-located with 44th European Conference on Information Retrieval*.
* Turki, H., Dossou, B. F. P., Emezue, C. C., Owodunni, A., Hadj Taieb, M. A., Ben Aouicha, M., Ben Aouicha, M., Ben Hassen, H., & Masmoudi, A. (2023). MeSH2Matrix: Combining MeSH keywords and machine learning for biomedical relation classification based on PubMed. *Scientometrics* (Forthcoming).

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
  - models/NeuralNets/*: contains training and validation source code for the D-Modeel in our work (a Fully Connected Nueral Network). Both models are trained with 195 classes and 5 grouped classes
  - models/ConvNets/*: contains training and validation source code for the C-Net model in our work ( a convolutional neural network). Both models are trained with 195 classes and 5 grouped classes.
  - models/TradiMlModels: Traditional ML models like SVM.
  - models/get_pretrained_weights.py: Download pretrained weights of neural nets.
  ## Computing  the Intergeted Gradients used for this work.
  - All the codes use to compute the Integrated Gradients for feature analysis are in the evaluation section of each model's code.
  - Note that training and evaluation for the C-Net moodel was done in the same notebook.
  - Also, we only did extensive feature analysis for the 5 grouped-classes.
