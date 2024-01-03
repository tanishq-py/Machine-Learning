import seaborn as sns
df=sns.load_dataset("tips")
df.head()

df.corr()
sns.heatmap(df.corr())

# JoinPlot
# A join plot allows to study the relationship between 2 numeric variables.
# The central chart display their correlation. It is usually a scatterplot, a hexbin plot, a 2D histogram or a 2D density plot
# Univariate Analysis
sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')
sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')

# Pair plot
# A “pairs plot” is also known as a scatterplot, 
# in which one variable in the same data row is matched with another variable's value,
# like this: Pairs plots are just elaborations on this, showing all variables paired with all the other variables
sns.pairplot(df)
sns.pairplot(df,hue='sex')

# Dist plot
# Dist plot helps us to check the distribution of the columns feature
sns.distplot(df['tip'])
sns.distplot(df['tip'],kde=False,bins=10)

# Categorical Plots
# Seaborn also helps us in doing the analysis on Categorical Data points. In this section we will discuss about
# boxplot
# violinplot
# countplot
# bar plot

# Count plot
df['sex'] = df['sex'].astype('category')
sns.countplot('sex',data=df)
# Count plot
sns.countplot(y='sex',data=df)
# Bar plot
sns.barplot(x='total_bill',y='sex',data=df)
# Bar plot
sns.barplot(x='sex',y='total_bill',data=df)
#Box plot
sns.boxplot('smoker','total_bill', data=df)
sns.boxplot(x="day", y="total_bill", data=df,palette='rainbow')
sns.boxplot(data=df,orient='v')
# categorize my data based on some other categories
sns.boxplot(x="total_bill", y="day", hue="smoker",data=df)

# Violin Plot
# Violin plot helps us to see both the distribution of data in terms of Kernel density estimation and the box plot
sns.violinplot(x="total_bill", y="day", data=df,palette='rainbow')
