import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

#Read the data of the deaths between the years 2002nand the year 2008
df2 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2002.csv')
df3 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2003.csv')
df4 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2004.csv')
df5 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2005.csv')
df6 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2006.csv')
df7 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2007.csv')
df8 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2008.csv')

#Join the datasets into only one datasets
frames = [df2, df3, df4, df5, df6, df7, df8]
death_2002_2008 = pd.concat(frames)

#Drop the rows that contains value Total from the datasets
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Medical_District_EN'] == 'Total'], inplace = True)
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Nationality_EN'] == 'Total'], inplace = True)
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Sex_EN'] == 'Total'], inplace = True)
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Cause_of_Death_EN'] == 'Total'], inplace = True)

#Keep only the english columns and remove the arabic columns
death_2002_2008 = death_2002_2008[['Year','Medical_District_EN','Cause_of_Death_EN','Nationality_EN','Sex_EN','Value']]


#create a dataframe that contains the sum of the deaths
death_2002_2008_total=death_2002_2008.groupby(['Year'])['Value'].sum().reset_index()
death_2002_2008_total_gender=death_2002_2008.groupby(['Year','Sex_EN'])['Value'].sum().reset_index()

#read the data of cancer_death between the year 2011 and 2018
cancer_death_2011_2018=pd.read_csv('cancer-mortality-ds-.csv')
#remove the arabic columns
cancer_death_2011_2018 = cancer_death_2011_2018[['Year','Emirate En','Cause Of Death En','Nationality Group En','Gender En','Total Deaths']]
#change the columns name
cancer_death_2011_2018 = cancer_death_2011_2018.rename(columns={'Year':'year','Emirate En':'district', 'Cause Of Death En': 'cause', 'Nationality Group En': 'nationality','Gender En':'gender','Total Deaths':'deaths'})

#read the death data from 2011 to cancer_death_2011_2018
deaths_2011_2018=pd.read_csv('death-counts-by-gender-nationality-and-emirate-v2.csv')
#remove the arabic columns
deaths_2011_2018 = deaths_2011_2018 [['Year','Emirate En','Nationality Group En','Gender En', 'Total']]
#rename the columns
deaths_2011_2018 = deaths_2011_2018.rename(columns={'Year':'year','EmirateEn':'district', 'Nationality Group En':'nationality','Gender En':'gender','Total':'total'})

#read the  birth data from 2002 to death_2002_2008
df12=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2002.csv')
df13=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2003.csv')
df14=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2004.csv')
df15=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2005.csv')
df16=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2006.csv')
df17=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2007.csv')
df18=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2008.csv')

#join the birth dast from 2002 to 2008 into 1 DataFrame
frames1 = [df12, df13, df14, df15, df16, df17, df18]
new_birth_2002_2008 = pd.concat(frames1)

#delete the rows with Total
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Region_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Birth_Status_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Nationality_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Delivery_Condition_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Delivery_Method_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Births'] == 'Total'], inplace = True)

#keep only the english columns
new_birth_2002_2008 = new_birth_2002_2008[['Year','Region_EN','Birth_Status_EN','Nationality_EN','Delivery_Condition_EN','Delivery_Method_EN','Births']]

#read the staff data (doctor ..)
staff=pd.read_csv('health-care-staff-by-emirate-sector-gender-and-job-category-ds.csv')
#keep only the english columns
staff = staff [['Year','Emirate En','Sector En','Category En','Gender En','Total']]
#change the name column for easier names
staff = staff.rename(columns={'Year':'year','Emirate En':'district', 'Sector En': 'sector', 'Category En': 'category','Gender En':'gender','Total':'total'})
# drop null values from the total column
staff = staff.dropna(subset=['total'])

#read the hospitals data
hospitals=pd.read_csv('number-of-beds-and-hospitals-by-health-sector-ds.csv')
#keep only the english columns
hospitals = hospitals [['Year','Emirate En','Sector En','Total Beds','Total Hospitals']]
# change the columns name for easier names
hospitals = hospitals.rename(columns={'Year':'year','Emirate En':'district','Sector En':'sector','Total Beds':'beds','Total Hospitals':'hospitals'})
#drop na if available
hospitals = hospitals.dropna(subset=['beds'])
hospitals = hospitals.dropna(subset=['hospitals'])




#make the user to enter the password to show the analysis
password = st.sidebar.text_input("Enter the password please", type="password")

if password == 'MsBa%42%':

    st.title('Health Care Analysis in the United Arab Emirates:')

    st.set_option('deprecation.showPyplotGlobalUse', False)

    #add a radio buttons options on the sidebar for the user to select what he wants to see
    button=st.sidebar.radio('Select which Analysis Date you want to See:',
                                ('Dates Between 2002 and 2008', 'Dates Between 2011 and 2018'))

    if button == 'Dates Between 2002 and 2008':

        #add a second radio button to filter based on the different analysis in this date
        button1=st.sidebar.radio('Select which Analysis you want to see:',
                                    ('Analysis of Death Cases based on the Cause, Gender Location','Analysis of New Born Babies','Analysis of Blood Units usage'))



        if button1 == 'Analysis of Death Cases based on the Cause, Gender Location':


            #add a gender filter in the sidebar
            gender_selection = st.sidebar.selectbox(
                    'Select the Gender you want to see',
                    ('All','Male','Female'))


            if gender_selection == 'All':

                col1, col2 = st.beta_columns(2)

                col1.subheader("Total Number of Deaths:")

                col1.write('In the below plot we can see that the number of deaths in the years 2002 to 2008 is approximately equal in and the range is between 2500 and 3000 deaths in year.')

                col2.subheader("Deaths Based on Gender:")

                col2.write('In the below plot we can see that in all the years the number of deaths for male are more than double from the number of deaths of female.')



                #barplot that shows the total number of deaths
                plt.rcParams['figure.figsize'] = [10, 8]
                death_2002_2008_total_bar=sns.barplot(x="Year", y="Value",color="Blue",data=death_2002_2008_total)
                death_2002_2008_total_bar.set(ylim=(0, 3500))
                death_2002_2008_total_bar.set(xlabel='Year',ylabel='Total Deaths')
                death_2002_2008_total_bar.set_title('Total Number of Deaths',y=1.02)
                col1.pyplot(use_column_width=True)

                death_2002_2008_total_gender_bar=sns.barplot(x="Year", y="Value",palette='Blues_d', color='blue', hue='Sex_EN', data=death_2002_2008_total_gender)
                death_2002_2008_total_gender_bar.set(ylim=(0, 3500))
                death_2002_2008_total_gender_bar.set(xlabel='Year',ylabel='Total Deaths')
                death_2002_2008_total_gender_bar.set_title('Total Number of Deaths based on Gender',y=1.02)
                col2.pyplot(use_column_width=True)


                col3, col4 = st.beta_columns(2)
                col3.subheader("Top Causes of Deaths")

                col4.subheader("Deaths Based on the selected causes")


                x = col3.number_input('Enter the number of causes you want to see:',min_value=3,)
                x=int(x)
                death_2002_2008_total_cause=death_2002_2008.groupby(['Cause_of_Death_EN'])['Value'].sum().reset_index()
                death_2002_2008_total_cause_top=death_2002_2008_total_cause.nlargest(x, ['Value'])
                col3.write('In the below plot we see the number of deaths based on the top causes in all the years from 2002 to 2008.')
                plt.rcParams['figure.figsize'] = [10, 8]
                death_2002_2008_total_cause_top_bar=sns.barplot(x='Cause_of_Death_EN', y='Value',color='Blue', data=death_2002_2008_total_cause_top)
                death_2002_2008_total_cause_top_bar.set(xlabel='Cause of Death',ylabel='Total Deaths')
                death_2002_2008_total_cause_top_bar.set_title('Total Number of Deaths per Cause',y=1.02)
                plt.xticks(rotation=70)
                col3.pyplot()



                cause_selection=death_2002_2008.copy()
                cause_selection_unique=cause_selection.drop_duplicates(subset=['Cause_of_Death_EN'])
                list = cause_selection_unique['Cause_of_Death_EN'].to_numpy()
                options = col4.multiselect('Select Cause of Death: (You can select more than 1)', list)
                options_df=pd.DataFrame(options,columns = ['Cause_of_Death_EN'])
                cause_selection_selected=pd.merge(death_2002_2008_total_cause, options_df, how='inner' )
                if not options:
                    col4.warning('Please add cause above.')
                elif options:
                    col4.write('In the below plot we see the deaths based on the selected causes in all the years from 2002 to 2008.')
                    cause_selection_selected_bar=sns.barplot(x="Cause_of_Death_EN", y="Value", color="Blue", data=cause_selection_selected)
                    cause_selection_selected_bar.set(xlabel='Generation',ylabel='Total Transactions')
                    cause_selection_selected_bar.set_title('Total Transactions based on Generation',y=1.02)
                    plt.xticks(rotation=60)
                    col4.pyplot()

            elif gender_selection == 'Male':

                #filter the data based on the Male
                death_2002_2008_M=death_2002_2008[death_2002_2008['Sex_EN']=='M']
                #count the deaths of Men
                death_2002_2008_M_toal=death_2002_2008_M.groupby(['Year'])['Value'].sum().reset_index()

                #plot the cases of death of Menplt.rcParams['figure.figsize'] = [13, 10]
                death_2002_2008_M_toal_bar=sns.barplot(x="Year", y="Value",color="Blue",data=death_2002_2008_M_toal)
                death_2002_2008_M_toal_bar.set(ylim=(0, 3500))
                death_2002_2008_M_toal_bar.set(xlabel='Year',ylabel='Total Deaths')
                death_2002_2008_M_toal_bar.set_title('Total Number of Deaths of Men',y=1.02)
                #st.pyplot()

                col1, col2 = st.beta_columns(2)
                col1.subheader("Top Causes of Deaths for Men:")

                col2.subheader("Deaths Based on the selected causes for Men:")

                #Check the top causes of death on the men
                x = col1.number_input('Enter the number of causes you want to see:',min_value=3,)
                x=int(x)
                death_2002_2008_M_cause=death_2002_2008_M.groupby(['Cause_of_Death_EN'])['Value'].sum().reset_index()
                death_2002_2008_M_cause_top=death_2002_2008_M_cause.nlargest(x, ['Value'])
                death_2002_2008_M_cause_top_bar=sns.barplot(x='Cause_of_Death_EN', y='Value',color='Blue', data=death_2002_2008_M_cause_top)
                death_2002_2008_M_cause_top_bar.set(xlabel='Cause of Death',ylabel='Total Deaths')
                death_2002_2008_M_cause_top_bar.set_title('Total Number of Deaths per Cause',y=1.02)
                plt.xticks(rotation=70)
                col1.pyplot()

                #make the user enter the cause to see the numbers
                cause_selection_M=death_2002_2008_M.copy()
                cause_selection_M_unique=cause_selection_M.drop_duplicates(subset=['Cause_of_Death_EN'])
                list_M = cause_selection_M_unique['Cause_of_Death_EN'].to_numpy()
                options_M = col2.multiselect('Select Cause of Death: (You can select more than 1)', list_M)
                options_M_df=pd.DataFrame(options_M,columns = ['Cause_of_Death_EN'])
                cause_selection_selected_M=pd.merge(death_2002_2008_M_cause, options_M_df, how='inner' )
                if not options_M:
                    col2.warning('Please add cause above.')
                elif options_M:
                    cause_selection_selected_M_bar=sns.barplot(x="Cause_of_Death_EN", y="Value", color="Blue", data=cause_selection_selected_M)
                    cause_selection_selected_M_bar.set(xlabel='Generation',ylabel='Total Transactions')
                    cause_selection_selected_M_bar.set_title('Total Transactions based on Generation',y=1.02)
                    plt.xticks(rotation=60)
                    col2.pyplot()


            elif gender_selection == 'Female':

                col1, col2 = st.beta_columns(2)
                col1.subheader("Top Causes of Deaths for Women:")

                col2.subheader("Deaths Based on the selected causes for Women:")

                #filter the data based on the Female
                death_2002_2008_F=death_2002_2008[death_2002_2008['Sex_EN']=='F']
                #count the deaths of Female
                death_2002_2008_F_toal=death_2002_2008_F.groupby(['Year'])['Value'].sum().reset_index()

                #plot the cases of death of Menplt.rcParams['figure.figsize'] = [13, 10]
                death_2002_2008_F_toal_bar=sns.barplot(x="Year", y="Value",color="Blue",data=death_2002_2008_F_toal)
                death_2002_2008_F_toal_bar.set(ylim=(0, 3500))
                death_2002_2008_F_toal_bar.set(xlabel='Year',ylabel='Total Deaths')
                death_2002_2008_F_toal_bar.set_title('Total Number of Deaths of Women',y=1.02)
                #st.pyplot()

                #Check the top causes of death on the Female
                st.subheader('The Top Causes of the Death for Women')
                x = col1.number_input('Enter the number of causes you want to see:',min_value=3,)
                x=int(x)
                death_2002_2008_F_cause=death_2002_2008_F.groupby(['Cause_of_Death_EN'])['Value'].sum().reset_index()
                death_2002_2008_F_cause_top=death_2002_2008_F_cause.nlargest(x, ['Value'])
                death_2002_2008_F_cause_top_bar=sns.barplot(x='Cause_of_Death_EN', y='Value',color='Blue', data=death_2002_2008_F_cause_top)
                death_2002_2008_F_cause_top_bar.set(xlabel='Cause of Death',ylabel='Total Deaths')
                death_2002_2008_F_cause_top_bar.set_title('Total Number of Deaths per Cause',y=1.02)
                plt.xticks(rotation=70)
                col1.pyplot()

                #make the user enter the cause to see the numbers
                cause_selection_F=death_2002_2008_F.copy()
                cause_selection_F_unique=cause_selection_F.drop_duplicates(subset=['Cause_of_Death_EN'])
                list_F = cause_selection_F_unique['Cause_of_Death_EN'].to_numpy()
                options_F = col2.multiselect('Select Cause of Death: (You can select more than 1)', list_F)
                options_F_df=pd.DataFrame(options_F,columns = ['Cause_of_Death_EN'])
                cause_selection_selected_F=pd.merge(death_2002_2008_F_cause, options_F_df, how='inner' )
                if not options_F:
                    col2.warning('Please add cause above.')
                elif options_F:
                    cause_selection_selected_F_bar=sns.barplot(x="Cause_of_Death_EN", y="Value", color="Blue", data=cause_selection_selected_F)
                    cause_selection_selected_F_bar.set(xlabel='Generation',ylabel='Total Transactions')
                    cause_selection_selected_F_bar.set_title('Total Transactions based on Generation',y=1.02)
                    plt.xticks(rotation=60)
                    col2.pyplot()

        elif button1 == 'Analysis of New Born Babies':

            col1, col2 = st.beta_columns(2)

            col1.subheader('Number of Births from 2002 to 2008 in All Nationality:')
            col2.subheader('Number of Births from 2002 to 2008 Based on Nationality:')

            col1.write('From the below plot we can see that the year has the lowest number of births then we reached a maximum in 2005 to decrese to ahlf in 2006 and after that we have an increse again lower to the previous increases.')

            new_birth_2002_2008_total=new_birth_2002_2008.groupby(['Year'])['Births'].sum().reset_index()
            new_birth_2002_2008_total_bar=sns.barplot(x="Year", y="Births",color="Blue",data=new_birth_2002_2008_total)
            new_birth_2002_2008_total_bar.set(ylim=(0, 30000))
            new_birth_2002_2008_total_bar.set(xlabel='Year',ylabel='Total Births')
            new_birth_2002_2008_total_bar.set_title('Total Number of Births',y=1.02)
            col1.pyplot()

            col2.write('From the below plot, we can see that in the years 2002, 2004, 2005 and 2008 the Non-Citizen births are higher, while in the other years the Citizen is higher with a huge differnece in the year of 2003.')

            new_birth_2002_2008_total_Nationality=new_birth_2002_2008.groupby(['Year','Nationality_EN'])['Births'].sum().reset_index()
            new_birth_2002_2008_total_Nationality_bar=sns.barplot(x="Year", y="Births",palette='Blues_d' , hue='Nationality_EN',data=new_birth_2002_2008_total_Nationality)
            new_birth_2002_2008_total_Nationality_bar.set(ylim=(0, 20000))
            new_birth_2002_2008_total_Nationality_bar.set(xlabel='Year',ylabel='Total Births')
            new_birth_2002_2008_total_Nationality_bar.set_title('Total Number of Births based on Nationality',y=1.02)
            col2.pyplot()




    elif button == 'Dates Between 2011 and 2018':

        button3=st.sidebar.radio('Select which Analysis you want to see:',
                                    ('Cancer Analysis (Cases, Death, Cause)','Analysis of the Healthcare system in UAE'))

        if button3 == 'Cancer Analysis (Cases, Death, Cause)':

            col1, col2 = st.beta_columns(2)

            col1.subheader("Total Number of Deaths:")

            deaths_2011_2018_total = deaths_2011_2018.groupby(['year'])['total'].sum().reset_index()

            deaths_2011_2018_total_bar=sns.barplot(x="year", y="total",color="Blue",data=deaths_2011_2018_total)
            deaths_2011_2018_total_bar.set(ylim=(0, 10000))
            deaths_2011_2018_total_bar.set(xlabel='Year',ylabel='Total Deaths')
            deaths_2011_2018_total_bar.set_title('Total Number of Deaths',y=1.02)
            col1.pyplot(use_column_width=True)

            col2.subheader("Deaths From Cancer")

            cancer_death_2011_2018_total = cancer_death_2011_2018.groupby(['year'])['deaths'].sum().reset_index()
            cancer_death_2011_2018_total_bar=sns.barplot(x="year", y="deaths",color="Blue",data=cancer_death_2011_2018_total)
            cancer_death_2011_2018_total_bar.set(ylim=(0, 2000))
            cancer_death_2011_2018_total_bar.set(xlabel='Year',ylabel='Total Deaths')
            cancer_death_2011_2018_total_bar.set_title('Total Number of Cancer Deaths',y=1.02)
            col2.pyplot(use_column_width=True)


            col1.subheader('The Top Causes Cancer of Death:')
            x = col1.number_input('Enter the number of causes you want to see:',min_value=3,)
            x=int(x)
            cancer_death_2011_2018_cause=cancer_death_2011_2018.groupby(['cause'])['deaths'].sum().reset_index()
            cancer_death_2011_2018_cause_top=cancer_death_2011_2018_cause.nlargest(x, ['deaths'])
            cancer_death_2011_2018_cause_bar=sns.barplot(x='cause', y='deaths',color='Blue', data=cancer_death_2011_2018_cause_top)
            cancer_death_2011_2018_cause_bar.set(xlabel='Cause of Cancer Death',ylabel='Total Deaths')
            cancer_death_2011_2018_cause_bar.set_title('Total Number of Deaths per Cancer Cause',y=1.02)
            plt.xticks(rotation=70)
            col1.pyplot()

            #make the user enter the cancer cause to see the numbers
            col2.subheader('Number of Deaths by each Cancer type:')
            cause_cancer_death_2011_2018=cancer_death_2011_2018.copy()
            cause_cancer_death_2011_2018_unique=cause_cancer_death_2011_2018.drop_duplicates(subset=['cause'])
            list_C = cause_cancer_death_2011_2018_unique['cause'].to_numpy()
            options_C = col2.multiselect('Select the Cancer Cause of Death: (You can select more than 1)', list_C)
            options_C_df=pd.DataFrame(options_C,columns = ['cause'])
            cancer_cause_selected=pd.merge(cause_cancer_death_2011_2018, options_C_df, how='inner' )
            cancer_cause_selected_total=cancer_cause_selected.groupby(['cause'])['deaths'].sum().reset_index()
            if not options_C:
                col2.warning('Please add cause above.')
            elif options_C:
                cancer_cause_selected_bar=sns.barplot(x="cause", y="deaths", color="Blue", data=cancer_cause_selected_total)
                cancer_cause_selected_bar.set(xlabel='Cause',ylabel='Number of Deaths per Cause')
                cancer_cause_selected_bar.set_title('Total Deaths by each Cancer type:',y=1.02)
                plt.xticks(rotation=60)
                col2.pyplot()


        elif button3 == 'Analysis of the Healthcare system in UAE':

            select1=st.sidebar.selectbox('Please select what you want to see (Hospitals or Staff Analysis)',
                                        ('Hospitals Analysis', 'Staff Analysis'))

            if select1 == 'Hospitals Analysis':

                hospitals_count=hospitals.groupby(['year','sector'])['hospitals'].sum().reset_index()

                hospitals_beds_count=hospitals.groupby(['year','sector'])['beds'].sum().reset_index()

                col1, col2 = st.beta_columns(2)

                col1.subheader('Number of Hospitals throughout the years in UAE:')
                hospitals_count_bar=sns.barplot(x="year", y="hospitals", palette='Blues_d', hue='sector', data=hospitals_count)
                hospitals_count_bar.set(xlabel='Year',ylabel='Number of Hospitals')
                hospitals_count_bar.set_title('Number of Hospitals in UAE based on Sector',y=1.02)
                col1.pyplot()

                col2.subheader('Number of Beds in Hospitals throughout the years in UAE:')
                hospitals_beds_count_bar=sns.barplot(x="year", y="beds", palette='Blues_d', hue='sector', data=hospitals_beds_count)
                hospitals_beds_count_bar.set(xlabel='Year',ylabel='Number of Beds in Hospitals')
                hospitals_beds_count_bar.set_title('Number of Beds in Hospitals in UAE based on Sector',y=1.02)
                col2.pyplot()

                st.write('Based on the above plots we can realize that the number of private hospitals is increasing more than the government hospitals throughout the years with a huge difference almost double in 2018, while the numbers of beds in the government hospitals is higher even in 2018.')

                st.write(hospitals)










if password != '123456':
    st.write('Please Enter the Correct Password from the Sidebar to display the Analysis')
