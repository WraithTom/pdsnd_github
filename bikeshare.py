import time
import pandas as pd
import numpy as np
import plotly.express as px



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello and welcome!\nLet\'s explore some US bikeshare data!')
##handle all the user input make city a global variable so it can be used in the user stats function
    while True:
        global city
        city = input("Do you want to look at data for Chicago, New York City or Washington?")
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Not an appropriate choice. Please try again")
        else:
            city = city.lower()
            break
    print("OK, {} data coming up!".format(city.title()))


    while True:
   
        month = input("Which month do you want to look at? You can choose from January to June or type 'all' to see everything.")
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Not an appropriate choice.")
        else:
            month = month.lower()
            break
    print("The month you have selected is: {} .".format(month.title()))

    while True:
        day = input("Finally what day of the week do you want to see? Again you can select 'all' to see everything.")
        if day.lower() not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday', 'all'):
            print("Not an appropriate choice.")
        else:
            day = day.lower()
            break
    print("The day we'll show is: {} .".format(day.title()))

    print('-'*40)
    return city, month, day   
    



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
         df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Frequent Month:', months[common_month -1])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day of the Week:', common_day)

    # TO DO: display the most common start hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

# Find the top 3 biggest hours
    popular_three = df['hour'].value_counts().nlargest(3)
        
    print('And the top three hours to start travelling are: ')
    print (popular_three)
   
    #try adding a bar chart to show the hours travelled
    print('\nThe chart below shows the number of trips by the start hour: ')
    fig = px.bar(df['hour'].value_counts(), title="Number of Bikeshare Trips by Hour Trip Started")
    fig.show() 
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    top_start = df['Start Station'].mode()[0]
    print('Most Frequent Station to Start at:', top_start)

    # TO DO: display most commonly used end station
    top_end = df['End Station'].mode()[0]
    print('Most Frequent Station to End at:', top_end)

    # TO DO: display most frequent combination of start station and end station trip
    df["Start_End"] = df["Start Station"] + " to " + df["End Station"]
    top_trip = df['Start_End'].mode()[0]
    print('Most Frequent Trip to and from:', top_trip)
    
    #Show the top 10 trips
    top_trips = df['Start_End'].value_counts().nlargest(10)
    print('\nThese are the 10 most popular trips:')
    print (top_trips)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time was:', f"{total_travel:,}", 'seconds, or',f"{total_travel/3600:,.1f}",'hours')


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average travel time was:', f"{mean_time:,}", 'seconds, or',f"{mean_time/60:,.1f}",'minutes')
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types    
    #count occurrence of user type
    users = df['User Type'].value_counts()

    #count occurrence of user type as percentage of total 
    user_percs = df['User Type'].value_counts(normalize=True)

    #concatenate results into one DataFrame
    freq = pd.concat([users,user_percs], axis=1, keys=['count', 'percentage'])
    print('\nThe number and percentage of trips by user type was:')
    print (freq)
    
    #handle missing data for washington

    if city.lower() != 'washington':


    # TO DO: Display counts of gender and percentages
        gen = df['Gender'].value_counts()
        gen_percs = df['Gender'].value_counts(normalize=True)
        gen_frq = pd.concat([gen,gen_percs], axis=1, keys=['count', 'percentage'])
        print('\nThe number and percentage of trips by gender of user was:')
        print (gen_frq)
    
   
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\na breakdown of users\' birth year and gender is as follows:' )
        fig2 = px.histogram(df, x="Birth Year", color='Gender',
            title="Year of Birth of Bikeshare Users by Gender")
        fig2.show()

        #Most common birth year
        mode_year = df['Birth Year'].mode()[0]
        print('The most common year of birth for users is:', mode_year)

        #Earliest birth year
        min_year = df['Birth Year'].min()
        print('The earliest year of birth for users is:', min_year)

        #latest birth year
        max_year = df['Birth Year'].max()
        print('The latest year of birth for users is:', max_year)
    else:
        print ('\nData for Gender and age of users are not available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def see_data(df): 
    yes_count = 0
    while True:
        show_head = input('\nDo you want to see raw data? Enter yes or no.\n')
        if show_head.lower() == 'yes':
            stats=df.iloc[yes_count:yes_count +5]
            print (stats)
            yes_count += 1*5
            break
        elif show_head.lower() != 'no':
            print ('sorry I do not understand that')
        else:
            break
        
    while True:
        if show_head.lower() == 'no':
            break
        else:
            show_head = input('\nDo you want to see some more raw data? Enter yes or no.\n')
            if show_head.lower() == 'yes':
                stats=df.iloc[yes_count:yes_count +5]
                print (stats)
                yes_count += 1*5
            elif show_head.lower() != 'no':
                print ('sorry I do not understand that')
            else:
                break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
   
        station_stats(df)
        
        trip_duration_stats(df)
        user_stats(df)
        
        see_data(df)
    

   
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
