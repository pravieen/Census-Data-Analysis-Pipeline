import streamlit as st
import pandas as pd


def get_connection():
    conn = st.connection("postgresql", type="sql")
    return conn
def execute_query(query):
    conn = get_connection()
    df = conn.query(query,ttl='10m')
    return pd.DataFrame(df)

# queries = {
#     '1) Total population of each district'                                                    : 'SELECT district, population as Total_Population FROM census;',
#     '2) Literate Males and Females in Each District'                                          : 'SELECT district, literate_male, literate_female FROM census;',
#     '3) Percentage of workers in each district'                                               : 'SELECT district, (male_workers/population * 100) AS male_worker_percentage, (female_workers/population * 100) AS femmale_worker_percentage FROM census',
#     '4) Households have access to LPG or PNG as a cooking fuel in each district?'             : 'SELECT district, lpg_or_png_households AS households_with_lpg_or_png FROM census',
#     '5) What is the religious composition of each district?'                                  : 'SELECT district, hindus, muslims, christians, sikhs, buddhists, jains, others_religions FROM census',
#     '6) How many households have internet access in each district?'                           : 'SELECT district,households_with_internet FROM census',
#     '7) What is the educational attainment distribution in each district?'                    : 'SELECT district, below_primary_education, primary_education, middle_education, secondary_education, higher_education, graduate_education, other_education, literate_education, illiterate_education FROM census',
#     '8) How many households have access to various modes of transportation in each district?' : 'SELECT district, households_with_bicycle, households_with_radio_transistor, households_with_scooter_motorcycle_moped, households_with_telephone_mobile_phone_landline_only, households_with_telephone_mobile_phone_mobile_only, households_with_tv_computer_laptop_telephone_mobile_phone_and_s, households_with_television, households_with_telephone_mobile_phone, households_with_telephone_mobile_phone_both FROM census',
#     '9) Condition of Occupied Census Houses in Each District'                                 : 'SELECT district_code, district, condition_of_occupied_census_houses_dilapidated_households AS dilapidated_houses, households_with_separate_kitchen_cooking_inside_house AS houses_with_kitchen, having_bathing_facility_total_households AS houses_with_bathing_facility, having_latrine_facility_within_the_premises_total_households AS houses_with_latrine_facility, not_having_bathing_facility_within_the_premises_total_households AS houses_without_bathing_facility, not_having_latrine_facility_within_the_premises_alternative_source_open_households AS houses_without_latrine_facility FROM census;',
#     '10) Household Size Distribution in Each District'                                        : 'SELECT district_code, district, household_size_1_person_households AS size_1_person, household_size_2_persons_households AS size_2_persons, household_size_3_to_5_persons_households AS size_3_to_5_persons, household_size_6_8_persons_households AS size_6_to_8_persons, household_size_9_persons_and_above_households AS size_9_and_above FROM census;',
#     '11) What is the total number of households in each state'                                : 'SELECT state_ut, SUM(households) AS total_households FROM census GROUP BY state_ut;',
#     '12) How many households have a latrine facility within the premises in each state?'      : 'SELECT state_ut, SUM(having_latrine_facility_within_the_premises_total_households) AS households_with_latrine_facility FROM census GROUP BY state_ut;',
#     '13) What is the average household size in each state?'                                   : 'SELECT state_ut, SUM(population) / SUM(households) AS average_household_size FROM census GROUP BY state_ut;',
# }
queries = {
    '1) Total population of each district'                                                                                    : 'SELECT district, population as Total_Population FROM census;',
    '2) Literate Males and Females in Each District'                                                                          : 'SELECT district, literate_male, literate_female FROM census;',
    '3) Percentage of workers in each district'                                                                               : 'SELECT district, (male_workers/population * 100) AS male_worker_percentage, (female_workers/population * 100) AS femmale_worker_percentage FROM census',
    '4) Households have access to LPG or PNG as a cooking fuel in each district?'                                             : 'SELECT district, lpg_or_png_households AS households_with_lpg_or_png FROM census',
    '5) What is the religious composition of each district?'                                                                  : 'SELECT district, hindus, muslims, christians, sikhs, buddhists, jains, others_religions FROM census',
    '6) How many households have internet access in each district?'                                                           : 'SELECT district,households_with_internet FROM census',
    '7) What is the educational attainment distribution in each district?'                                                    : 'SELECT district, below_primary_education, primary_education, middle_education, secondary_education, higher_education, graduate_education, other_education, literate_education, illiterate_education FROM census',
    '8) How many households have access to various modes of transportation in each district?'                                 : 'SELECT district, households_with_bicycle, households_with_radio_transistor, households_with_scooter_motorcycle_moped, households_with_telephone_mobile_phone_landline_only, households_with_telephone_mobile_phone_mobile_only, households_with_tv_computer_laptop_telephone_mobile_phone_and_s, households_with_television, households_with_telephone_mobile_phone, households_with_telephone_mobile_phone_both FROM census',
    '9) Condition of Occupied Census Houses in Each District'                                                                 : 'SELECT district_code, district, condition_of_occupied_census_houses_dilapidated_households AS dilapidated_houses, households_with_separate_kitchen_cooking_inside_house AS houses_with_kitchen, having_bathing_facility_total_households AS houses_with_bathing_facility, having_latrine_facility_within_the_premises_total_households AS houses_with_latrine_facility, not_having_bathing_facility_within_the_premises_total_households AS houses_without_bathing_facility, not_having_latrine_facility_within_the_premises_alternative_source_open_households AS houses_without_latrine_facility FROM census;',
    '10) Household Size Distribution in Each District'                                                                        : 'SELECT district_code, district, household_size_1_person_households AS size_1_person, household_size_2_persons_households AS size_2_persons, household_size_3_to_5_persons_households AS size_3_to_5_persons, household_size_6_8_persons_households AS size_6_to_8_persons, household_size_9_persons_and_above_households AS size_9_and_above FROM census;',
    '11) What is the total number of households in each state'                                                                : 'SELECT state_ut, SUM(households) AS total_households FROM census GROUP BY state_ut;',
    '12) How many households have a latrine facility within the premises in each state?'                                      : 'SELECT state_ut, SUM(having_latrine_facility_within_the_premises_total_households) AS households_with_latrine_facility FROM census GROUP BY state_ut;',
    '13) What is the average household size in each state?'                                                                   : 'SELECT state_ut, SUM(population) / SUM(households) AS average_household_size FROM census GROUP BY state_ut;',
    '14) How many households are owned versus rented in each state?'                                                          : 'SELECT state_ut, SUM(ownership_owned_households) AS owned_households, SUM(ownership_rented_households) AS rented_households FROM census GROUP BY state_ut;',
    '15) What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?' : 'SELECT state_ut, SUM(type_of_latrine_facility_pit_latrine_households) AS pit_latrine, SUM(type_of_latrine_facility_other_latrine_households) AS other_latrines, SUM(type_of_latrine_facility_flush_pour_flush_latrine_connected_to_other_system_households) AS flush_latrines, SUM(type_of_latrine_facility_night_soil_disposed_into_open_drain_households) AS night_soil_disposed FROM census GROUP BY state_ut;',
    '16) How many households have access to drinking water sources near the premises in each state?'                          : 'SELECT state_ut, SUM(location_of_drinking_water_source_near_the_premises_households) AS near_the_premises FROM census GROUP BY state_ut;',
    '17) What is the average household income distribution in each state based on the power parity categories?'               : 'SELECT state_ut, AVG(power_parity_less_than_rs_45000) AS avg_less_than_45000, AVG(power_parity_rs_45000_90000) AS avg_45000_to_90000, AVG(power_parity_rs_90000_150000) AS avg_90000_to_150000, AVG(power_parity_rs_150000_240000) AS avg_150000_to_240000, AVG(power_parity_rs_240000_330000) AS avg_240000_to_330000, AVG(power_parity_rs_330000_425000) AS avg_330000_to_425000, AVG(power_parity_above_rs_545000) AS avg_above_545000 FROM census GROUP BY state_ut;',
    '18) What is the percentage of married couples with different household sizes in each state?'                             : 'SELECT state_ut, SUM(married_couples_1_households) * 100.0 / SUM(households) AS percentage_1_couple, SUM(married_couples_2_households) * 100.0 / SUM(households) AS percentage_2_couples, SUM(married_couples_3_households) * 100.0 / SUM(households) AS percentage_3_couples, SUM(married_couples_3_or_more_households) * 100.0 / SUM(households) AS percentage_3_or_more_couples, SUM(married_couples_none_households) * 100.0 / SUM(households) AS percentage_no_couples FROM census GROUP BY state_ut;',
    '19) How many households fall below the poverty line in each state based on the power parity categories?'                 : 'SELECT state_ut, SUM(power_parity_less_than_rs_45000) AS below_poverty_line FROM census GROUP BY state_ut;',
    '20) What is the overall literacy rate (percentage of literate population) in each state?'                                : 'SELECT state_ut, SUM(literate) * 100.0 / SUM(population) AS literacy_rate_percentage FROM census GROUP BY state_ut;'
}

st.title("Census Data Analysis")
selected_query = st.sidebar.selectbox('Select a Query',list(queries.keys()))
if selected_query:
    st.subheader(selected_query)
    query = queries[selected_query]

    try:
        result_df = execute_query(query)
        st.dataframe(result_df, height=700,width=700,hide_index=True)
    except Exception as e:
        st.error(f"An error occurred while executing the query: {e}")

