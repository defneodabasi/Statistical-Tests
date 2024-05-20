# Statistical Analysis Document

In the .py file both functions used in statistical test and main function is present. 

The idea behind using these test is as follows:

The stat analysis code initiates a Shapiro-Wilk test to check the normality
in the data. If the data is normally distributed, an equal variance test (Levene’s
test) is conducted. This part is applicable for both small and large sample size
data.

Following the result of the Shapiro-Wilk test, if the data is not normally
distributed, a ‘Mann-Whitney U’ test is employed. In cases where distributions
are normal, but variances are unequal the code executes a ‘T-Test Unequal
Variance’ (also known as Welch’s test). This scenario assumes that both data
groups are sampled from Gaussian populations with different standard deviations. Conversely, if both data are normally distributed and variances are equal,
a ‘T-Test Equal Variance’ test is conducted. Here, the assumption is that both
groups are sampled from Gaussian populations with equal variances.

All tests yield a p-value, where a lower p-value signifies greater statistical
significance of observed differences. To be clearer, the p-value represents the
probability of obtaining observed results assuming both experiments belong to
the same population. A p-value below 0.05 indicates a high likelihood that
the experiments are statistically different, leading to the conclusion that the
differences between the experiments are statistically different. This code is
useful for comparing two experiment results statistically.
