#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies and Setup

import pandas as pd


# In[3]:


# File to Load (Remember to Change These)

school_data_to_load = "../Instructions/PyCitySchools/Resources/schools_complete.csv"
student_data_to_load = "../Instructions/PyCitySchools/Resources/students_complete.csv"


# In[4]:


# Read School and Student Data File and store into Pandas DataFrames

school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)


# In[5]:


#did you read and import the school data properly

school_data


# In[6]:


#did you read and import the student data properly

student_data


# In[7]:


# Combine the data into a single dataset.  

school_data_complete_df = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# In[8]:


school_data_complete_df


# In[9]:


#total number of schools

school_list = school_data_complete_df["school_name"].unique()
total_schools = len(school_list)
total_schools


# In[10]:


#total number of students

student_list = school_data_complete_df["student_name"]
total_students = len(student_list)
total_students


# In[11]:


#total budget (Correct Syntax)

total_budget = school_data_complete_df["budget"].sum()
total_budget


# In[12]:


#average math score 

average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[13]:


#average reading score 

average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[15]:


#passing math score >= 70%

passing_math_score = school_data_complete_df[school_data_complete_df["math_score"] >= 70]

number_math_passed = len(passing_math_score.index)

percentage_math_passed = number_math_passed / total_students

percentage_math_passed


# In[16]:


#passing reading score >= 70%

passing_reading_score = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]

number_reading_passed = len(passing_reading_score.index)

percentage_reading_passed = number_reading_passed / total_students

percentage_reading_passed


# In[17]:


#passing overall (both math and reading score >= 70%)

passing_overall_score = school_data_complete_df[(school_data_complete_df["reading_score"] >=70) & (school_data_complete_df["math_score"] >=70)]

passing_overall_count = len(passing_overall_score.index)

percentage_overall_passed = passing_overall_count / total_students

percentage_overall_passed


# In[18]:


#clean up strings, (), and []

final_results_df = pd.DataFrame({
    "Total Schools":[str(total_schools)],
    "Total Students": [str(total_students)],
    "Total Budget": [str(total_budget)],
    "Average Math Score": [str(average_math_score)],
    "Average Reading Score": [str(average_reading_score)],
    "% Passing Math": [str(percentage_math_passed)],
    "% Passing Reading": [str(percentage_reading_passed)],
    "% Overall Passing": [str(percentage_overall_passed)],
})

final_results_df


# In[30]:


school_data_complete_df


# In[33]:


school_names = school_data_complete_df.value_counts('school_name')
school_names


# In[36]:


school_type = school_data_complete_df.value_counts(['school_name', 'type'])
school_type


# In[44]:


#total_budget = school_data_complete_df.groupby('school_name').mean(['budget'])
total_budget = school_data_complete_df.groupby('school_name').mean()['budget']
total_budget


# In[46]:


per_student_budget = total_budget / school_names
per_student_budget


# In[50]:


avg_math_score = school_data_complete_df.groupby('school_name').mean()['math_score']
avg_math_score


# In[51]:


avg_reading_score = school_data_complete_df.groupby('school_name').mean()['reading_score']
avg_reading_score


# In[65]:


over_70_math = school_data_complete_df[school_data_complete_df['math_score'] >= 70]
over_70_math

school_count_math = over_70_math.groupby(['school_name']).count()['math_score']
school_count_math

percentage_math = school_count_math / school_names
percentage_math


# In[67]:


over_70_pass = school_data_complete_df[(school_data_complete_df["reading_score"] >=70) & (school_data_complete_df["math_score"] >=70)]
over_70_pass

school_count_pass = over_70_pass.groupby(['school_name']).count()['Student ID']
school_count_pass

percentage_pass = school_count_pass / school_names
percentage_pass


# In[68]:


school_results_df = pd.DataFrame({
    "School": school_names,
    #"Total Students": [str(total_students)],
    #"Total Budget": [str(total_budget)],
    #"Average Math Score": [str(average_math_score)],
    #"Average Reading Score": [str(average_reading_score)],
    #"% Passing Math": [str(percentage_math_passed)],
    #"% Passing Reading": [str(percentage_reading_passed)],
    #"% Overall Passing": [str(percentage_overall_passed)],
})

school_results_df


# In[ ]:




