amino_acid_counts_per_category = {'envelope': Counter(), 'membrane': Counter(), 'capsid': Counter()}

for coding_region in data['coding regions']:
  for category, aa_counter in amino_acid_counts_per_category.items():
    if category in coding_region['product'].lower():
      aa_counter.update(coding_region['translation'])

amino_freq_per_category = {}
aa_relative_freq_per_category = {}

for category, aa_counter in amino_acid_counts_per_category.items():
  aa_freq = normalize(aa_counter)
  aa_freq_per_category[category] = aa_freq
  aa_relative_freq = {aa:freq/all_aa_freq[aa] for aa, freq in aa_freq.items()}
  all_relative_freq_category[category] = aa_relative_freq

print(all_relative_freq_per_category)
