HPO Data Mapper

This tool automates the extraction and mapping of clinical phenotypes from unstructured medical notes to standardized Human Phenotype Ontology (HPO) terms. By converting clinical descriptions into HPO codes, this utility facilitates downstream genomic analysis and diagnostic prioritization.
🩺 Clinical Context - In medical genetics, "phenotyping" is the process of describing a patient's observable traits. Because different clinicians use different terminology, the Human Phenotype Ontology provides a standardized vocabulary. This mapper helps ensure that a term like "unusual heart rhythm" is consistently recorded as HP:0011675 (Arrhythmia).
🚀 Features

    Keyword Extraction: Identifies clinical terms within raw text files or notes.

    HPO Mapping: Cross-references extracted terms with the HPO database using exact and fuzzy matching.

    JSON/CSV Export: Outputs mapped terms in formats ready for clinical decision support tools or genomic pipelines.

    Clinical Note Parsing: Handles common medical abbreviations and formatting.

🛠️ Technical Stack

    Language: Python 3.x

    Key Libraries: json (provides tools to encode and decode data in JavaScript Object Notation)

    Data Sources: Utilizes the Human Phenotype Ontology database.
