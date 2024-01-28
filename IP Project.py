import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main_menu():
    print("WELCOME TO ATLAS EDUCATION")
    print("**************************")
    print("Read Data From File in Different Way")
    print("1. Read complete csv file")
    print("2. Reading complete file without index")
    print("===============")
    print("Dataframe Statistics Menu")
    print("3. Track the number of students who have emigrated from particular region")
    print("4. To see how manay Total Number of student emigrated in particulars year")
    print("5. To see the statistical measure which allows us to visualize the average number of students leaving in particular year")
    print("6. If you are looking for information about the Maximum number of students emigrating in particular year")
    print("7. If you are looking for information about the Minimum number of students emigrating in particular year ")
    print("8. you might be interested in finding the middle value of the emigration data set")
    print("===============")
    print("Data Visualization")
    print("10. Analysing with the help of Line Chart")
    print("11. Analysing with the help of Bar Plot")
    print("12. Analysing with the help of Pie chart")
    print("13. Analysing with the help of Scatter chart")
    print("===============")
    print("Apply Data Manipulation in the records of CSV file")
    print("14. Sorting the data as per your choice")
    print("15. Read Top and Bottom Records from file as per requirment")
    print("16. Add the New Country Record in File")
    print("17. Search the Records as per Country Name")
    print("**************************")

#main_menu()
def Read_CSV():
    print("Reading Data from CSV file")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    print(df)
def no_index():
    print("Reading Data from CSV file without index value")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    print(df)
def cou_nt():
    print("Display Count function")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    print(df.count())
def sum():
    print("Display sum function")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    print(df.sum())
def mean():
    print("Display mean function")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    print(df.mean())
def ma_x():
    print("Display max function")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    print(df.max())
def mi_n():
    print("Display min function")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    print(df.min())
def meadia_n():
    print("Display median function")
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    print(df.meadian())
def line_plot():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    st1=df["NO OF STUDENT 2023"]
    st2=df["NO OF STUDENT 2022"]
    st3=df["NO OF STUDENT 2021"]
    con=df['Country']
    plt.xlabel("Country")
    plt.xticks(rotation='vertical')
    print("Select Specific Line Chart as given below:")
    print("press 1 to print the data for Country V/S 2023")
    print("press 2 to print the data for Country V/S 2022")
    print("press 3 to print the data for Country V/S 2021")
    op=int(input("Enter your choice:"))
    if op==1:
        plt.ylabel("NO OF STUDENT 2023")
        plt.title("Country V/S No of Indian student in 2023")
        plt.plot(con,st1)
        plt.show()
    elif op==2:
        plt.ylabel("NO OF STUDENT 2022")
        plt.title("Country V/S No of Indian student in 2022")
        plt.plot(con,st2)
        plt.show()
    elif op==3:
        plt.ylabel("NO OF STUDENT 2021")
        plt.title("Country V/S No of Indian student in 2021")
        plt.plot(con,st3)
        plt.show()
 
    else:
        print("Enter valid input")
def bar_plot():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    st1=df["NO OF STUDENT 2023"]
    st2=df["NO OF STUDENT 2022"]
    st3=df["NO OF STUDENT 2021"]
    con=df['Country']
    plt.xlabel("Country")
    plt.xticks(rotation='vertical')
    print("Select Specific Bar Chart as given below:")
    print("press 1 to print the data for Country V/S No of Indain Student2023")
    print("press 2 to print the data for Country V/S No of Indain Student2022")
    print("press 3 to print the data for Country V/S No of Indain Student2021")
    print("press 4 to print all the data in form of stack bar chart")
    print("press 5 to print all the data in form of multi bar chart")
    op=int(input("Enter your choice:"))
    if op==1:
        plt.ylabel("NO OF STUDENT 2023")
        plt.title("Country V/S No of Indian student in 2023")
        plt.bar(con,st1)
        plt.show()
    elif op==2:
        plt.ylabel("NO OF STUDENT 2022")
        plt.title("Country V/S No of Indian student in 2022")
        plt.bar(con,st2)
        plt.show()
    elif op==3:
        plt.ylabel("NO OF STUDENT 2022")
        plt.title("Country V/S No of Indian student in 2021")
        plt.bar(con,st3)
        plt.show()
    elif op==4:
        plt.ylabel("Graph for all data")#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        plt.bar(con,st1,label="Country V/S No of Indian student in 2023")
        plt.bar(con,st2,label="Country V/S No of Indian student in 2022")
        plt.bar(con,st3,label="Country V/S No of Indian student in 2021")
        plt.legend(loc='upper right')
        plt.show()
    elif op==5:
        con=np.arange(len(con))
        width=0.25
        plt.ylabel("Graph for all data")#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        plt.bar(con+0.25,st1,label="Country V/S No of Indian student in 2023")
        plt.bar(con+0.50,st2,label="Country V/S No of Indian student in 2022")
        plt.bar(con+0.50,st3,label="Country V/S No of Indian student in 2021")
        plt.legend(loc='upper right')
        plt.show()
    else:
        print("Enter valid input")
    
def pie_plot():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    st1=df["NO OF STUDENT 2023"]
    st2=df["NO OF STUDENT 2022"]
    st3=df["NO OF STUDENT 2021"]
    con=df['Country']
    plt.xlabel("Country")
    plt.xticks(rotation='vertical')
    print("Select Specific Pie Chart as given below:")
    print("press 1 to print the data for Country V/S NO OF STUDENT 2023")
    print("press 2 to print the data for Country V/S NO OF STUDENT 2022")
    print("press 3 to print the data for Country V/S NO OF STUDENT 2021")
    op=int(input("Enter your choice:"))
    if op==1:
        plt.title("Country V/S NO OF STUDENT 2023")
        plt.pie(st1,labels=con,autopct="%2d%%")
        #autopct attribute can be used to show the percentage of the data.
        plt.show()
    elif op==2:
        plt.pie(st2,labels=con,autopct="%3d%%")
        plt.title("Country V/S NO OF STUDENT 2022")
        plt.show()
    elif op==3:
        plt.pie(st3,labels=con,autopct="%3d%%")
        plt.title("Country V/S NO OF STUDENT 2021")
        plt.show()
    else:
        print("Enter valid input")
        
def scatter_chart():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    st1=df["NO OF STUDENT 2023"]
    st2=df["NO OF STUDENT 2022"]
    st3=df["NO OF STUDENT 2021"]
    con=df['Country']
    ax=plt.gca()
    ax.scatter(con,st1,color='b',label="Country V/S NO OF STUDENT 2023")
    ax.scatter(con,st2,color='r',label="Country V/S NO OF STUDENT 2022")
    ax.scatter(con,st3,color='k',label="Country V/S NO OF STUDENT 2021")
    plt.xlabel("Country")
    plt.xticks(rotation='vertical')
    plt.title("Complete Scatter chart")
    plt.legend(loc='upper right')
    plt.show()
def data_sorting():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    print("Press 1 to arrange the record as per the Country")
    print("Press 2 to arrange the record as per the NO OF STUDENT 2023")
    print("Press 3 to arrange the record as per the NO OF STUDENT 2022")
    print("Press 4 to arrange the record as per the NO OF STUDENT 2021")
    op=int(input("Enter Your choice:"))
    if op==1:
        df.sort_values(["Country"],inplace=True)
        #inplace: make the changes in passed DataFrame
        print(df)
    elif op==2:
        df.sort_values(["NO OF STUDENT 2023"],inplace=True)
        print(df)
    elif op==3:
        df.sort_values(["NO OF STUDENT 2022"],inplace=True)
        print(df)
    elif op==4:
        df.sort_values(["NO OF STUDENT 2021"],inplace=True)
        print(df)
    else:
        print("Enter valid input")
def top_bottom_selected_records():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv",index_col=0)
    top=int(input("How many records to display from top:"))
    print("First",top,"records")
    print(df.head(top))
    bottom=int(input("How many records to display from bottom:"))
    print("Last",bottom,"records")
    print(df.tail(bottom))
def AddNewCountry():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    df["NO OF STUDENT 2023"]=df["NO OF STUDENT 2023"].astype('int')
    df["NO OF STUDENT 2023"]=df["NO OF STUDENT 2023"].astype('int')
    df["NO OF STUDENT 2023"]=df["NO OF STUDENT 2023"].astype('int')
    print(df)
    #Enter all the details which present in csv file
    C_name=input("Country=")
    stu1=int(input("Enter NO OF STUDENT 2023="))
    stu2=int(input("Enter NO OF STUDENT 2022="))
    stu3=int(input("Enter NO OF STUDENT 2021="))
    #To get total number of records present in csv file, will store in n
    n=df["Country"].count()
    #To add all the details 
    df.loc[n]=[C_name,stu1,stu2,stu3]
    df.to_csv("C:/Users/Manav/Downloads/final_data.csv",index=False)
    df["NO OF STUDENT 2023"]=df["NO OF STUDENT 2023"].astype('int')
    df["NO OF STUDENT 2022"]=df["NO OF STUDENT 2022"].astype('int')
    df["NO OF STUDENT 2021"]=df["NO OF STUDENT 2021"].astype('int')
    print(df)
def SearchState():
    df=pd.read_csv("C:/Users/Manav/Downloads/final_data.csv")
    df.to_csv("C:/Users/Manav/Downloads/final_data.csv",index=False)
    df["NO OF STUDENT 2023"]=df["NO OF STUDENT 2023"].astype('int')
    df["NO OF STUDENT 2022"]=df["NO OF STUDENT 2022"].astype('int')
    df["NO OF STUDENT 2021"]=df["NO OF STUDENT 2021"].astype('int')
    print(df)
    #print(df)
    cname=input("Enter Country Name:")
    #To store state name in variable c
    c=df.loc[df["Country"]==cname]
    if c.empty:
        print("No Record Found With the State name:",cname)
    else:
        print("Details with State Name:",cname)
        print(c)

#Main Menu

def enter_ch():
    opt=int(input("enter your choice="))
    if opt==1:
        Read_CSV()
    elif opt==2:
        no_index()
    elif opt==3:
        cou_nt()
    elif opt==4:
        sum()
    elif opt==5:
        mean()
    elif opt==6:
        ma_x()
    elif opt==7:
        mi_n()
    elif opt==8:
        media_n()
    elif opt==9:
        mo_d()
    elif opt==10:
        line_plot()
    elif opt==11:
        bar_plot()
    elif opt==12:
        pie_plot()
    elif opt==13:
        scatter_chart()
    elif opt==14:
        data_sorting()
    elif opt==15:
        top_bottom_selected_records()
    elif opt==16:
        AddNewCountry()
    elif opt==17:
        SearchState()  
        print("enter valid input")

main_menu()
enter_ch()

for i in range(1,100,1):
    con=input("Do you want to Continue?(Y/N) : ")

    if(con=='Y' or con=='y'):
        main_menu()
        enter_ch()
    else:
        print("Invalid Input")
        break
      



    
        
