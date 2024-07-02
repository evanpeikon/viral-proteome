from operator import itemgetter

def get_amino_acid_stats(aa, category):
  return '%s: freq ratio= %.2f, freq in category = %.4f, general freq = %.4f' % (aa, \ aa_relative_frequency_per_category[category][aa], aa_freq_per_category[category][aa], all_aa_freq[aa])

for category, aa_relative_freq in aa_relative_freq_per_category.items():
  max_aa, _ = max(aa_relative_freq.items(), key= itemgetter(1))
  min_aa, _ = min(aa_relative_freq.items(), key= itemgetter(1))
  print('%s:' % category)
  print('\t' + get_aa_states(max_aa, category)
  print('\t' + get_aa_states(min_aa, category)
