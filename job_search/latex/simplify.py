import re
import argparse

acronym_dict = {
    "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics": "ACL",
    "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing": "EMNLP",
    "Transactions of the Association for Computational Linguistics": "TACL",
    "Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)": "NAACL",
    
    "Findings of the Association for Computational Linguistics: EMNLP 2022": "Findings of EMNLP",
    "Findings of the Association for Computational Linguistics: EACL 2023": "Findings of EACL",
    "Findings of the Association for Computational Linguistics: ACL 2023": "Findings of ACL",
    
    "Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP": "BlackboxNLP",
    
    "The Twelfth International Conference on Learning Representations": "ICLR",
    "International Conference on Machine Learning": "ICML",
    "Advances in Neural Information Processing Systems": "NeurIPS",
    
    "Conference on Computer Vision and Pattern Recognition": "CVPR",
    "European Conference on Computer Vision": "ECCV",
    # Add more mappings here as needed
}

def replace_titles_with_acronyms(bibtex_content):
    def replace_match(match):
        entry = match.group(0)
        for full_title, acronym in acronym_dict.items():
            if full_title in entry:
                entry = entry.replace(full_title, acronym)
        return entry

    # Regular expression to match `booktitle` and `journal` fields
    pattern = re.compile(r'(booktitle|journal)\s*=\s*\{[^}]*\}', re.IGNORECASE)
    
    # Replace full titles with acronyms
    updated_content = pattern.sub(replace_match, bibtex_content)
    return updated_content


def main():
    parser = argparse.ArgumentParser(description="Process a BibTeX file to simplify journal and conference titles and remove URL and pages fields.")
    parser.add_argument("--input_file", help="The input BibTeX file")
    parser.add_argument("--output_file", help="The output BibTeX file")
    
    args = parser.parse_args()
    
    # Read the input BibTeX file
    with open(args.input_file, 'r') as file:
        bib_content = file.read()

    # Process the BibTeX content
    updated_content = replace_titles_with_acronyms(bib_content)

    # Write the processed content to the output file
    with open(args.output_file, 'w') as file:
        file.write(updated_content)

    print(f"Processed BibTeX file saved to {args.output_file}")

if __name__ == "__main__":
    main()
