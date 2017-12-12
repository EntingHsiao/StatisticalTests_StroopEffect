
# coding: utf-8

# ### Analyzing the Stroop Effect
# Perform the analysis in the space below. Remember to follow [the instructions](https://docs.google.com/document/d/1-OkpZLjG_kX9J6LIQ5IltsqMzVWjh36QpnP2RYpVdPU/pub?embedded=True) and review the [project rubric](https://review.udacity.com/#!/rubrics/71/view) before submitting. Once you've completed the analysis and write up, download this file as a PDF or HTML file and submit in the next section.
# 
# 
# (1) What is the independent variable? What is the dependent variable?

# --write answer here--
# 
# The independent variable is whether the words are under congruent condition.
# 
# The dependent variable is the time it takes for the participants to name the ink colors of the words in equally-sized lists.
# 
# 

# (2) What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.

# --write answer here--
# 
# The null hypotheses: the time it takes for the participants to name the ink colors of the words under the incongruent words condition is the same as or less than the time it takes to name the ink colors of the words under the congruent word conditions. In other words, there's no difference or decrease between the congruent task and the incongruent task.
#  
# The alternative hypotheses: the time it takes for the participants to name the ink colors of the words under the incongruent words condition is longer than the time it takes to name the ink colors of the words under the congruent word conditions. In other words, there's some increase between the congruent task and the incongruent task.
# 
# $H_0: \mu_d \leq 0 $
# 
# $H_a: \mu_d > 0 $    
# 
# where $\mu_d$ is the difference of population means between the sample of the congruent task and the sample of incongruent task.
#  
# I will use one tailed paired T-test for the reasons below:
# 
# 1) The population mean and the population standard deviation are unknown.
# 
# 2) The distribution of the dataset is not heavily skewed.
# 
# 3) The sample size is less than 30. 
# 
# 4) According to the Wiki page of the Stroop effect, the purpose of the experiment is to investigate if the reaction time is longer in incongruent task, so the statistical test will focus on the increase in reaction time. In order to maximize the ability to detect the increase, I opt for a one-tailed test. 
# 
# 5) The dataset contains each participant’s performance in both congruent and incongruent tasks, which means the result of each participant is measured twice, resulting in pairs of observations, so the paired T-test should be used in this circumstance.  
# 
#   
# There are some assumptions for the paired T test:
# 
# 1)The difference between pairs should be approximately normally distributed.
# 
# 2)The data is randomly collected from a selected portion of the total population.
# 
# 3)The data are continuous (interval/ratio).
# 
# 

# (3) Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability. The name of the data file is 'stroopdata.csv'.

# In[3]:


# Perform the analysis here
import pandas as pd

df = pd.read_csv('stroopdata.csv')
print('The median of the reaction time in congruent task', df['Congruent'].median())
print('The median of the reaction time in incongruent task', df['Incongruent'].median())
print ('The mean of the reaction time in congruent task',df['Congruent'].mean() )
print ('The mean of the reaction time in incongruent task', df['Incongruent'].mean())
print ('The standard deviation of the reaction time in congruent task', df['Congruent'].std() )
print ('The standard deviation of the reaction time in incongruent task', df['Incongruent'].std())
print ('The variance of the reaction time in congruent task', df['Congruent'].var() )
print ('The variance deviation of the reaction time in incongruent task', df['Incongruent'].var())


# --write answer here--
# 
# The median of the reaction time in congruent task 14.3565
# 
# The median of the reaction time in incongruent task 21.0175
# 
# The mean of the reaction time in congruent task 14.051125
# 
# The mean of the reaction time in incongruent task 22.0159166667
# 
# The standard deviation of the reaction time in congruent task 3.55935795765
# 
# The standard deviation of the reaction time in incongruent task 4.79705712247
# 
# The variance of the reaction time in congruent task 12.6690290707
# 
# The variance deviation of the reaction time in incongruent task 23.0117570362

# (4) Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[4]:


# Build the visualizations here
get_ipython().magic('pylab inline')
import seaborn as sns

sns.distplot(df['Congruent'], label='Congruent')
sns.distplot(df['Incongruent'], label='Incongruent', axlabel='Reaction time')
plt.legend()


# --write answer here--
# 
# From the distribution plot above, we can see the observations from the incongruent task sample has a higher mean than those from the congruent task sample,and the distribution of the congruent is almost a normal distribution. 

# (5) Now, perform the statistical test and report the results. What is the confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

# In[5]:


# Perform the statistical test here
import scipy as sp

#Because this is a paired T-test, so the first step is to calculate the difference (di = yi − xi) 
#between the two observations on each pair, making sure you distinguish between positive and negative differences.
df['Difference']=df['Incongruent']-df['Congruent']

t_value, p_value = sp.stats.ttest_1samp(df['Difference'],0)
critical_value= sp.stats.t.ppf(.95,23)#The alpha value is 0.05
print ('T value',t_value)
print ('P value', p_value/2)#the default function is two tailed test, so the value has to be divided by two for the one tailed test.'
print ('Critical value',critical_value)



# --write answer here--
# 
# One-tailed paired T-test result:
# The confidence level = 95%(p<0.05), the critical value:1.71387
# 
# T value: 8.020706944109957
# 
# P value: 0.000000002
# 
# According to the statistics above, the null hypotheses should be rejected because 
# 1) The T value is a positive value, 8.020706944109957, which means the incongruent task takes more time than the congruent task.
# 2) the P value(0.000000002) of the test is less than the alpha value(0.05), which means the difference between the two samples is significant.
#  
# The result match I expectation; when I tried the Stroop task, the time it took for the incongruent task is almost three times more than the congruent one. The Stroop effect worked significantly for me, so the test result did matched my expectation.  
# 
# 
# 

# References: 
# 
# FAQ: What Are the Differences Between One-Tailed and Two-Tailed Tests?, UCLA,
# https://stats.idre.ucla.edu/other/mult-pkg/faq/general/faq-what-are-the-differences-between-one-tailed-and-two-tailed-tests/
# 
# 
# List of LaTeX Mathematical Symbols, Oeis.org
# https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols
# 
# 
# One Sample T-test, NCSS Statistical Software, https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/NCSS/One-Sample_T-Test.pdf
# 
# 
# Stroop Effect, Wikipedia, https://en.wikipedia.org/wiki/Stroop_effect
# 
# 
# Statistics: 1.1 Paired T-tests, Shier, Rosie,http://www.statstutor.ac.uk/resources/uploaded/paired-t-test.pdf
# 
# 
# Scipy.stats.ttest_1samp, SciPy.org,  https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ttest_1samp.html
# 
# 
# Scipy.stats.t, SciPy.org,
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.t.html
# 
# 
# Visualizing the Distribution of a Dataset, seaborn.pydata.org, https://seaborn.pydata.org/tutorial/distributions.html
# 
# 
# What Statistical Analysis Should I Use? Statistical Analyses Using STATA, UCLA,
# https://stats.idre.ucla.edu/stata/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-stata/
# 
# 
# 

# In[ ]:




