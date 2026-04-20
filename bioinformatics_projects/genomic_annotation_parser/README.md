Gales Genomic Annotation Parser

This utility was developed as part of the UCSD Bioinformatics Fundamentals curriculum to automate the extraction and annotation of genomic variants from Gales platform data exports. It streamlines the transition from raw sequencing outputs to annotated datasets ready for clinical interpretation.
🧬 Project Overview - In clinical workflows, raw data often comes in platform-specific formats that require cleaning and standardization before they can be used in downstream analysis. 
This project focuses on:

    Data Extraction: Parsing complex text/CSV exports from the Gales platform.

    Functional Annotation: Mapping variants to biological insights, such as gene impact and functional consequences.

    Database Integration: Preparing parsed data for ingestion into relational databases (MySQL/MariaDB).

🚀 Features

    Automated Parsing: Replaces manual data entry by programmatically extracting variant metadata.

    Relational Mapping: Structures flat-file data into logical schemas for efficient querying.

    Error Handling: Validates data consistency during the parsing process to ensure data integrity.

🛠️ Technical Implementation

    Language: Python

    Environment: *NIX Command Line

    Concepts: Regular Expressions (Regex), File I/O, and Relational Database Design.
