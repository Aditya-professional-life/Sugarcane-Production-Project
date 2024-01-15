#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[42]:


df = pd.read_csv("List of Countries by Sugarcane Production.csv")
df


# In[43]:


df.shape


# ## DATA Cleaning
# 
# replace "."(dots) with "," comma 

# In[44]:


df["Production (Tons)"] = df["Production (Tons)"].str.replace(".",",")
df["Production per Person (Kg)"]  = df["Production per Person (Kg)"].str.replace(".",",")
df["Acreage (Hectare)"] = df["Acreage (Hectare)"].str.replace(".",",")
df["Yield (Kg / Hectare)"]  = df["Yield (Kg / Hectare)"].str.replace(".",",")
df


# In[45]:


df.sample()


# In[46]:


df = df.drop("Unnamed: 0",axis = 1)
df


# In[47]:


df.rename(columns={"Production (Tons)": "Production(Tons)"}, inplace=True)
df.rename(columns={"Production per Person (Kg)": "Production_per_person(Kg)"}, inplace=True)
df.rename(columns={"Acreage (Hectare)": "Acreage(Hectare)"}, inplace=True)
df.rename(columns={"Yield (Kg / Hectare)": "Yield(Kg/Hectare)"}, inplace=True)

df.head()


# In[ ]:





# In[48]:


df.isnull().sum()


# In[49]:


df[df["Acreage(Hectare)"].isnull()]


# In[50]:


df = df.dropna().reset_index(drop=True)
df


# In[51]:


df.nunique()


# In[52]:


df.dtypes


# In[53]:


# Remove commas and convert to float for "Production(Tons)"
df["Production(Tons)"] = df["Production(Tons)"].str.replace(',', '').astype(float)

# Repeat the process for other columns if needed
df["Production_per_person(Kg)"] = df["Production_per_person(Kg)"].str.replace(',', '').astype(float)
df["Acreage(Hectare)"] = df["Acreage(Hectare)"].str.replace(',', '').astype(float)
df["Yield(Kg/Hectare)"] = df["Yield(Kg/Hectare)"].str.replace(',', '').astype(float)

df.head()


# In[54]:


df.dtypes


# ## Univariate Analysis

# In[55]:


df.head()


# ## How many contreies produce sugarcane from each continent?

# In[56]:


df["Continent"].value_counts()


# In[57]:


df["Continent"].value_counts().plot(kind = "bar")


# africa have maxium number of countries whch produces sugarcane

# In[58]:


df.describe()


# ## checking for outliers

# In[59]:


plt.figure(figsize = (10,8))
plt.subplot(2,2,1)
sns.boxplot(df["Production(Tons)"])
plt.title("production(Tons)")

plt.subplot(2,2,2)
sns.boxplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")

plt.subplot(2,2,3)
sns.boxplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")

plt.subplot(2,2,4)
sns.boxplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")

plt.show()


# we have outliers in the data but outliers are required here as it shows the countries which has maximum production. And then we can see what are the reasons for outliers.

# In[60]:


df.describe()


# In[ ]:





# In[61]:


plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
sns.distplot(df["Production(Tons)"])
plt.title("Production(Tons)")

plt.subplot(2, 2, 2)
sns.distplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")

plt.subplot(2, 2, 3)
sns.distplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")

plt.subplot(2, 2, 4)
sns.distplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")

plt.tight_layout()  # Adjust subplot parameters for better layout
plt.show()


# In[62]:


sns.violinplot(df["Production(Tons)"])


# Bivarite Analysis

# In[63]:


# df_new = df_new = df[["Country","Prouction(Tons)"]].set_index("country")
df_new = df[["Country", "Production(Tons)"]].set_index("Country")
df_new


# In[64]:


df_new["Production(Tons)_percent"] = df_new["Production(Tons)"]*100/df_new["Production(Tons)"].sum()
df_new


# In[65]:


df_new["Production(Tons)_percent"].plot(kind = "pie",autopct="%.2f")


# brazil india and Chine have 65% of production of sugarcane

# In[66]:


df[["Country", "Production(Tons)"]].set_index("Country").sort_values("Production(Tons)", ascending=False)


# In[67]:


df_new["Production(Tons)"].head(10).plot(kind = "bar")


# In[68]:


ax = sns.barplot(data = df.head(10),x = "Country",y="Production(Tons)")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.show()


# In[69]:


ax = sns.barplot(data = df.head(10),x = "Country",y="Acreage(Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.show()


# brazil have the herighest production 

# ##  Which country has highest yield per hectare?

# In[70]:


df_yield = df.sort_values("Yield(Kg/Hectare)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Yield(Kg/Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# In[71]:


df_yield = df.sort_values("Production_per_person(Kg)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Production_per_person(Kg)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# Production per Person in highest in Paraguay

# In[72]:


df


# In[78]:


numeric_df = df.select_dtypes(include='number')
correlation_matrix = numeric_df.corr()

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="Greens", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()


# Do countries with highest land produce more sugarcane?

# In[79]:


sns.scatterplot(data = df, x = "Acreage(Hectare)", y = "Production(Tons)", hue = "Continent" )


# Do countries which yield more sugarcane per hectare produces more sugarcane in total?

# In[80]:


sns.scatterplot(data = df, x = "Yield(Kg/Hectare)" , y = "Production(Tons)", hue = "Continent")


# Analysis for Continent

# In[83]:


df_continent = df.groupby("Continent").sum()
df_continent["number_of_countries"] = df.groupby("Continent").count()["Country"]
df_continent


# Which continent produces maximum sugarcane?

# In[84]:


df_continent["Production(Tons)"].sort_values(ascending =  False).plot(kind = "bar")


# Do number of countries in a Continent effects production of sugarcane?

# In[85]:


continent_names = df_continent.index.to_list()
sns.lineplot(data = df_continent,x = "number_of_countries", y= "Production(Tons)" )
plt.xticks(df_continent["number_of_countries"], continent_names, rotation =90)
plt.show()


# Do continent with highest land produces more sugarcane?

# In[86]:


sns.lineplot(data = df_continent,x = "Acreage(Hectare)", y= "Production(Tons)" )


# Production distribution by continent

# In[87]:


df_continent["Production(Tons)"].plot(kind = "pie", autopct = "%.2f%%")
plt.title('Production Distribution by Continent')
plt.show()


# In[90]:


numeric_df_continent = df_continent.select_dtypes(include='number')
correlation_matrix_continent = numeric_df_continent.corr()
correlation_matrix_continent

