from pymongo import MongoClient
import psycopg2  

client = MongoClient('mongodb://localhost:27017/')
db = client['census_data']
collection = db['census']
data = list(collection.find())

hostname = 'localhost'
port_id = 5432
database = 'task5'
username = 'postgres'
pwd = 'Prakavdha@2002'

conn = psycopg2.connect(
    host=hostname, 
    port=port_id, 
    password=pwd, 
    dbname=database,
    user = username
)

cur = conn.cursor()

create_script = '''CREATE TABLE IF NOT EXISTS census (
    district_code INT PRIMARY KEY,
    state_ut VARCHAR(255),
    district VARCHAR(255),
    population FLOAT,
    male FLOAT,
    female FLOAT,
    literate FLOAT,
    literate_male FLOAT,
    literate_female FLOAT,
    sc FLOAT,
    male_sc FLOAT,
    female_sc FLOAT,
    st FLOAT,
    male_st FLOAT,
    female_st FLOAT,
    workers FLOAT,
    male_workers FLOAT,
    female_workers FLOAT,
    main_workers FLOAT,
    marginal_workers FLOAT,
    non_workers FLOAT,
    cultivator_workers FLOAT,
    agricultural_workers FLOAT,
    household_workers FLOAT,
    other_workers FLOAT,
    hindus FLOAT,
    muslims FLOAT,
    christians FLOAT,
    sikhs FLOAT,
    buddhists FLOAT,
    jains FLOAT,
    others_religions FLOAT,
    religion_not_stated FLOAT,
    lpg_or_png_households FLOAT,
    households_with_electric_lighting FLOAT,
    households_with_internet FLOAT,
    households_with_computer FLOAT,
    households_rural FLOAT,
    households_urban FLOAT,
    households FLOAT,
    below_primary_education FLOAT,
    primary_education FLOAT,
    middle_education FLOAT,
    secondary_education FLOAT,
    higher_education FLOAT,
    graduate_education FLOAT,
    other_education FLOAT,
    literate_education FLOAT,
    illiterate_education FLOAT,
    total_education FLOAT,
    young_and_adult FLOAT,
    middle_aged FLOAT,
    age_group_50 FLOAT,
    age_not_stated FLOAT,
    households_with_bicycle FLOAT,
    households_with_car_jeep_van FLOAT,
    households_with_radio_transistor FLOAT,
    households_with_scooter_motorcycle_moped FLOAT,
    households_with_telephone_mobile_phone_landline_only FLOAT,
    households_with_telephone_mobile_phone_mobile_only FLOAT,
    households_with_tv_computer_laptop_telephone_mobile_phone_and_scooter_car FLOAT,
    households_with_television FLOAT,
    households_with_telephone_mobile_phone FLOAT,
    households_with_telephone_mobile_phone_both FLOAT,
    condition_of_occupied_census_houses_dilapidated_households FLOAT,
    households_with_separate_kitchen_cooking_inside_house FLOAT,
    having_bathing_facility_total_households FLOAT,
    having_latrine_facility_within_the_premises_total_households FLOAT,
    ownership_owned_households FLOAT,
    ownership_rented_households FLOAT,
    type_of_bathing_facility_enclosure_without_roof_households FLOAT,
    type_of_fuel_used_for_cooking_any_other_households FLOAT,
    type_of_latrine_facility_pit_latrine_households FLOAT,
    type_of_latrine_facility_other_latrine_households FLOAT,
    type_of_latrine_facility_night_soil_disposed_into_open_drain_households FLOAT,
    type_of_latrine_facility_flush_pour_flush_latrine_connected_to_other_system_households FLOAT,
    not_having_bathing_facility_within_the_premises_total_households FLOAT,
    not_having_latrine_facility_within_the_premises_alternative_source_open_households FLOAT,
    main_source_of_drinking_water_uncovered_well_households FLOAT,
    main_source_of_drinking_water_handpump_tubewell_borewell_households FLOAT,
    main_source_of_drinking_water_spring_households FLOAT,
    main_source_of_drinking_water_river_canal_households FLOAT,
    main_source_of_drinking_water_other_sources_households FLOAT,
    main_source_of_drinking_water_other_sources_spring_river_canal_tank_pond_lake_other_sources_households FLOAT,
    location_of_drinking_water_source_near_the_premises_households FLOAT,
    location_of_drinking_water_source_within_the_premises_households FLOAT,
    main_source_of_drinking_water_tank_pond_lake_households FLOAT,
    main_source_of_drinking_water_tapwater_households FLOAT,
    main_source_of_drinking_water_tubewell_borehole_households FLOAT,
    household_size_1_person_households FLOAT,
    household_size_2_persons_households FLOAT,
    household_size_1_to_2_persons FLOAT,
    household_size_3_persons_households FLOAT,
    household_size_3_to_5_persons_households FLOAT,
    household_size_4_persons_households FLOAT,
    household_size_5_persons_households FLOAT,
    household_size_6_8_persons_households FLOAT,
    household_size_9_persons_and_above_households FLOAT,
    location_of_drinking_water_source_away_households FLOAT,
    married_couples_1_households FLOAT,
    married_couples_2_households FLOAT,
    married_couples_3_households FLOAT,
    married_couples_3_or_more_households FLOAT,
    married_couples_4_households FLOAT,
    married_couples_5_households FLOAT,
    married_couples_none_households FLOAT,
    power_parity_less_than_rs_45000 FLOAT,
    power_parity_rs_45000_90000 FLOAT,
    power_parity_rs_90000_150000 FLOAT,
    power_parity_rs_45000_150000 FLOAT,
    power_parity_rs_150000_240000 FLOAT,
    power_parity_rs_240000_330000 FLOAT,
    power_parity_rs_150000_330000 FLOAT,
    power_parity_rs_330000_425000 FLOAT,
    power_parity_rs_425000_545000 FLOAT,
    power_parity_rs_330000_545000 FLOAT,
    power_parity_above_rs_545000 FLOAT,
    total_power_parity FLOAT,
    total_religion FLOAT
) '''

cur.execute(create_script)

with open('/Users/a.s.pravieen/Desktop/DE Project/t4/updated_census_data.csv','r') as f:
    cur.copy_expert('COPY census FROM STDIN WITH CSV HEADER', f)

conn.commit()
conn.close()

