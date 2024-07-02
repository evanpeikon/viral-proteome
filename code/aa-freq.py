from collections import Counter

def normalize(counter):
  total = sum(counter.values())
  return {key: count/total for key, count in counter.items()}

amino_acid_counter = Counter()

for coding_region in data['coding_regions']:
  amino_acid_counter.update(coding_region['translation'])

amino_acid_frequencies = normalize(amino_acid_counter)
print(amino_acid_frequencies)
