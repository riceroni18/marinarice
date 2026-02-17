def calculate_gc_content(sequence):
    """Calculates the percentage of G and C bases in a DNA sequence."""
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')

    if len(sequence) == 0:
        return 0

    gc_content = (g_count + c_count) / len(sequence) * 100
    return round(gc_content, 2)

def parse_fasta(filename):
    """Reads a FASTA file and prints the GC content for each sequence found."""
    print(f"--- Analyzing File: {filename} ---")

    with open(filename, 'r') as file:
        label = ""
        sequence = ""

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # If we hit a new label, process the previous sequence first
                if label:
                    gc = calculate_gc_content(sequence)
                    print(f"Sequence: {label} | Length: {len(sequence)} bp | GC Content: {gc}%")

                label = line[1:] # Remove the '>'
                sequence = ""   # Reset for the new sequence
            else:
                sequence += line

        # Process the very last sequence in the file
        if label:
            gc = calculate_gc_content(sequence)
            print(f"Sequence: {label} | Length: {len(sequence)} bp | GC Content: {gc}%")

parse_fasta("sample.fasta.py")
