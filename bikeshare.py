import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january',
              'february',
              'march',
             'april',
             'may',
             'june',
             'all']

DAY_LIST = ['monday',
              'tuesday',
              'wednesday',
             'thursday',
             'friday',
             'saturday',
            'sunday',
            'all']

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

    city = ''

    while city not in CITY_DATA.keys():
        print("\nWould you like to see data for Chicago, New York City or Washington? Please type the name of the city:")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nNot valid. Please check your input.")
            print("\nRestarting...")

    print(f"\nYou have chosen {city.title()} to analyze.")
    
    # TO DO: get user input for month (all, january, february, ... , june)

    month = ''
    
    while month not in MONTH_DATA:
        print("\nPlease enter the month, between January to June or all you want to explore:")
        month = input().lower()

        if month not in MONTH_DATA:
            print("\nNot valid. Please check your input.")
            print("\nRestarting...")

    print(f"\nYou have chosen {month.title()} to filter by.")    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ''
    
    while day not in DAY_LIST:
        print("\nPlease type which day of the week or all you want to explore: ")
        day = input().lower()

        if day not in DAY_LIST:
            print("\nNot valid. Please check your input.")
            print("\nRestarting...")
    print(f"\nYou have chosen {day.title()} to filter by.")
    
    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
    #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTH_DATA.index(month) + 1
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
    try:
        most_common_month_num = df['Start Time'].dt.month.mode()[0]
        most_common_month = MONTH_DATA[most_common_month_num-1].title()
        print(f"\nMost common month: {most_common_month}")
    except Exception as e:
        print('\nCould not calculate the most common month, as an error ocurred: {}'.format(e)) 
    
    # TO DO: display the most common day of week
    try:
        most_common_day = df['Start Time'].dt.weekday_name.mode()[0]
        print(f"\nMost common day of week: {most_common_day}")
    except Exception as e:
        print('Could not calculate the most common day of week, as an Error occurred: {}'.format(e))

    # TO DO: display the most common start hour
    try:
        most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
        print(f"\nMost common start Hour: {most_common_start_hour}")
    except Exception as e:
        print('Could not calculate the most common start hour, as an Error occurred: {}'.format(e))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        popular_start_station = df['Start Station'].mode()[0]
        print(f"\nMost commonly used start station:", popular_start_station)
    except Exception as e:
        print('Could not calculate the most commonly used start station, as an Error occurred: {}'.format(e))

    # TO DO: display most commonly used end station
    try:
        popular_end_station = df['End Station'].mode()[0]
        print(f'\nMost commonly used end station :', popular_end_station)
    except Exception as e:
        print('Could not calculate the most commonly used end station, as an Error occurred: {}'.format(e))
    
    # TO DO: display most frequent combination of start station and end station trip
    try:
        df['start to end station'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
        frequent_start_end = df [ 'start to end station'].mode()[0]
        print(f'\nMost frequent combination of start station and end station trip :', frequent_start_end)
    except Exception as e:
        print('Could not calculate the most frequent combination of start station and end station trip, as an Error occurred: {}'.format(e))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"\nThe total travel time is: {total_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    print(f"\nThe mean travel time is: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The counts of user types are:\n\n{user_type}")

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe counts of users genders are:\n\n{gender}")
    except:
        print("\nThere is no gender details considering the filters choosed.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details considering the filters choosed.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Displays raw data on bikeshare users if requested by the user."""
    i = 0
    raw = input("\nWould you like to see some raw data? Enter yes or no.\n").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        print(df.iloc[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
        raw = input('\nWould you like to see more raw data? Enter yes or no.\n').lower() # TO DO: convert the user input to lower case using lower() function
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()