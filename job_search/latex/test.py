import re

# Comprehensive dictionary for major AI conferences and journals
replacements = {
    "Transactions of the Association for Computational Linguistics": "TACL",
    "International Conference on Learning Representations": "ICLR",
    "Conference on Empirical Methods in Natural Language Processing": "EMNLP",
    "Association for Computational Linguistics": "ACL",
    "Conference on Computer Vision and Pattern Recognition": "CVPR",
    "International Conference on Machine Learning": "ICML",
    "Advances in Neural Information Processing Systems": "NeurIPS",
    "European Conference on Computer Vision": "ECCV",
    "Annual Meeting of the Association for Computational Linguistics": "ACL",
    "North American Chapter of the Association for Computational Linguistics": "NAACL",
    "Conference on Neural Information Processing Systems": "NeurIPS"
}

# Function to simplify the title of a given BibTeX entry
def simplify_title_version(title):
    for long, short in replacements.items():
        # Use regex to match the full phrase that might include details and replace it with the abbreviation
        pattern = re.compile(r'.*\b' + re.escape(long) + r'\b.*', re.IGNORECASE)
        if pattern.search(title):
            title = short
            break
    return title

# Test cases
test_titles = [
    "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    "The Twelfth International Conference on Learning Representations"
]

# Applying the function to test cases
simplified_titles = [simplify_title_version(title) for title in test_titles]

# Print results
for original, simplified in zip(test_titles, simplified_titles):
    print(f"Original: {original}")
    print(f"Simplified: {simplified}\n")
