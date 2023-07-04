# LRRK2-bioactivity-prediction

Parkinson’s disease is a chronic neudegenerative disease that is characterised by the loss of
dopamine producing neurons in a specific region of the brain known as substantia nigra. The
patients suffer from rigidity in muscles, tremors, bradykinesia and impaired posture and
balance. While the exact cause of the disease remains unclear, studies show that genetic as
well as environmental factors contribute to the manifestation of the disorder. One protein that
has been implicated in the progression and pathogenesis of Parkinson’s Disease is
Leucine-rich repeat kinase 2. This project aimed to develop a Quantitative Structure-Activity
Relationship (QSAR) study that used a novel dataset from chEMBL. The biological activity
data was retrieved and preprocessed to label compounds as active, inactive, or intermediate
based on their IC50 values. The dataset was subjected to various preprocessing methods
before Exploratory data analysis was performed to understand the distribution of molecules
in chemical space, and chemical space analysis was conducted using the Lipinski descriptors.
Molecular descriptors were calculated using the PaDEL-Descriptor software, and the dataset
was prepared for model building. Finally, a regression model was built using Random Forest
algorithm, and its performance was evaluated through data visualisation. This project
demonstrates the usefulness of QSAR models in drug discovery to predict the biological
activity of small molecules. The model was eventually deployed as a web application for
researchers to use.
