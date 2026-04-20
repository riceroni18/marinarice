 # Genomic Annotation Pipeline (GALES)

This project demonstrates the transition from manual web-based biological analysis to automated, command-line driven pipelines. It utilizes the **GALES (Genomic Analysis and Labeled Extraction System)** pipeline, an open-source tool used extensively in the Human Microbiome Project.

## 🛠️ Key Competencies
* **Command Line Orchestration:** Moving beyond web interfaces to execute biological computations via the terminal.
* **Software Implementation:** Installing and configuring bioinformatics toolkits and libraries (Biocode).
* **Data Wrangling:** "Massaging" biological data formats (GFF3, FASTA) to ensure compatibility between piped tools.
* **Production Workflows:** Executing robust, multi-step annotation pipelines used in large-scale reference genome projects.

## 🧬 Pipeline Overview
The workflow chains multiple tools to perform functional genomic annotation. This project explores the balance between "black box" pipeline execution and the technical necessity of understanding intermediate data transformations.

### 🧬 Gene Prediction with Prodigal
I utilized **Prodigal** (Prokaryotic Dynamic Programming Genefinding Algorithm) to identify protein-coding genes within the assembly. 

**Command executed:**
`prodigal -f gff -i unit2_new_genome.fasta -o unit2_new_genome.prodigal.gff`


**Technical Choice:**
The `-f gff` flag was specified to ensure the output adheres to the **GFF3 standard**, allowing for seamless integration into downstream functional annotation tools and genome browsers.
🛠️ Technical Implementation

    Language: Python

    Environment: *NIX Command Line

    Concepts: Regular Expressions (Regex), File I/O, and Relational Database Design.
