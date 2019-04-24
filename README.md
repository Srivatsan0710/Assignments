```r
# Differential Correlation algorithm

function: Differential_Correlation
  # Number of bootstraps = 1000
  # Input : Gene pairs. n x 2 matrix where rows contain expression of the respective genes from 
  # column 1 and column 2 for the samples in AD, followed by Controls.
  # Output : 2 p-values for the two distributions, 1000 correlation values for resampled values
  # for every bootstrap iteration

  Find the Spearman's correlation values between the two genes (column 1 and column 2) for the 
  respective samples in AD and Controls - r_AD, r_CTL

  Initialize b = 1 #Indicating number of bootstraps

  Initialize count_AD = count_CTL = 0 #Initialize counts to 0

  Initialize cor_resampled_AD, cor_resampled_CTL #A vector of length 1000 to store the 
  correlation values after resampling in AD and Controls respectively in each iteration.

  loop:
      Resample the columns randomly in both AD and Controls 
      Calculate Spearman's correlation values using the resampled values - r_AD', r_CTL'
      append r_AD' to cor_resampled_AD
      append r_CTL' to cor_resampled_CTL
      count_AD = count_AD + ifelse(r_AD > r_CTL, r_CTL' >= r_AD, r_CTL' <= r_AD)
      count_CTL = count_CTL + ifelse(r_CTL > r_AD, r_AD' >= r_CTL, r_AD' <= r_CTL)
  till b = 1000

  #Calculting p-value for the two distributions
  p_value_AD = 2 * count_AD / 1000
  p_value_CTL = 2 * count_CTL / 1000

  return p_value_AD, p_value_CTL, cor_resampled_AD, cor_resampled_CTL

for every significant gene pairs:
    call Differential_Correlation()
    Adjust p_value_AD and p_value_CTL using Benjamini-Hochberg method
    if max(p_value_AD, p_value_CTL) <= 0.05:
          Add the current edge as 'Differentially Correlated'
```
