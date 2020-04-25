import time
import pandas as pd
import numpy as np
from datetime import datetime

print('The program below was written with the help of the lessons taught in this nanodegree program, and also with helpful information and blog discussions in StackOverFlow, Pandas Documentation in PyData and programizer.com')


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
    print('Hello! Let\'s explore some US bikeshare data!')

 # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city\'s data would you like to explore?:        ').lower()
        if city in CITY_DATA:
            print('Ok, {} it is'.format(city.capitalize()))
            break
        else:

            print('Not a valid name. Try another')

    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'All']

        # TO DO: get user input for month (all, january, february, ... , june)(
    while True:
        month = input('Which month\s data would you like to review? Write \"All" if you want to see everything:   ').title()
        if month in Months:
            print('Alright, {}'.format(month.capitalize()))
            break
        else:
            print('Not a valid month. Try another')

    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

        # TO DO: get user input for month (all, january, february, ... , june)(
    while True:
        day = input('Which day of the week data would you like to see? Write \"All" if you want to see everything:    ').title()
        if day in day_of_week:
            print('Yay! I love, {}s'.format(day))
            break
        else:
            print('Not a valid day. Try another')


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
    df = pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'All']
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    index_month_common = df['month'].mode()[0]
    common_month = months[int(index_month_common) - 1]

    print('THe most common month for trips in bikeshare is: {}'.format(common_month))


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week for trips is: {}'.format(common_day_of_week))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is usually around: {}'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: {}'.format(top_start_station))

    # TO DO: display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: {}'.format(top_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + ' and ' + df['End Station']
    top_combo = df['combo'].mode()[0]
    print('The most frequent combination of start and ending stations is: {}'.format(top_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    total_travel_time = (total_travel/60)
    print('Total travel time is:', total_travel_time, 'mins or {} hours.'.format(total_travel_time/60))


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The Average trip duration is {} secs or {} mins'.format(mean_travel, mean_travel/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_counts = df['User Type'].value_counts()
    print('Each User Type presents the following count:')
    print(type_counts)

    # TO DO: Display counts of gender

    def gender(df):
        """Counts how many female and male cases are in the database"""
        try:
            gender_count = df['Gender'].value_counts()
            print('Each gender presents the following count: (Remember there are missing cases)')
            print(gender_count)
        except:
            print('This city does not have user\'s gender information')


    def BirthY(dataframe):
        """Revises which is the earliest, most recent and most common Birth Year"""
        try:
            birthyear = df['Birth Year']
            earliest = int(birthyear.min())
            recent = int(birthyear.max())
            common = int(birthyear.mode()[0])
            print('Let\'s check some stats about the birth years of the bike users.....')
            print('Here we go! {} is the earliest, {} most recent and {} the most common birthyear'.format(earliest, recent, common))
            return(earliest, recent, common)

        except:
            print('This city does not have birthyears information')
    # TO DO: Display earliest, most recent, and most common year of birth

    gender(df)
    BirthY(df)

    print('Would you like to see a data sample of 5 trips? ')
    while True:
            choice = input('Type yes or no to display sample:  ').lower()
            if choice == 'yes':
                df_elements = df.sample(n=5)
                print(df_elements)

            else:
                 print('Ok, no')
                 break
#------------------------
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
print('This bikeshare project is being used for a new github project')
