# Census Data Standardization and Analysis Pipeline  

## **Overview**  
This project focuses on cleaning, processing, and analyzing census data to ensure uniformity, accuracy, and accessibility. It covers tasks like data standardization, missing data handling, database integration, and interactive visualization.

## **Features**  
- Rename columns and states for consistency.  
- Handle missing data using logical calculations.  
- Standardize new state/UT formations (e.g., Telangana, Ladakh).  
- Save processed data in MongoDB and transfer it to a relational database.  
- Query the database and present results on a Streamlit dashboard.  

## **Technologies Used**  
- **Languages:** Python, SQL  
- **Databases:** MongoDB, MySQL  
- **Visualization Tool:** Streamlit  

## **Dataset**  
The dataset can be found here: [https://drive.google.com/drive/folders/10FLf8dEXqz_vc8p4DVoA5MKAh60gp1f6](#)  

## **Project Structure**  


## **Tasks and Solutions**  
### **Task 1: Rename Column Names**  
Renamed columns for uniformity. For example:  
- `State name` → `State/UT`  
- `Male_Literate` → `Literate_Male`  
- `Rural_Households` → `Households_Rural`  

### **Task 2: Rename State/UT Names**  
Converted all-caps state/UT names to proper case (e.g., `ANDHRA PRADESH` → `Andhra Pradesh`).  

### **Task 3: Handle New State/UT Formation**  
Handled data for Telangana (2014) and Ladakh (2019) by renaming districts from their parent states.  

### **Task 4: Handle Missing Data**  
Used formulas to fill missing data, e.g.:  
- `Population = Male + Female`  
- `Literate = Literate_Male + Literate_Female`  

Stored the percentage of missing data before and after processing.  

### **Task 5: Save Data to MongoDB**  
Saved the processed data to a MongoDB collection named `census`.  

### **Task 6: Database Connection**  
Fetched data from MongoDB and uploaded it to a relational database (MySQL).  

### **Task 7: Run SQL Queries**  
Executed queries to analyze the census data. Examples:  
- Total population by district.  
- Percentage of workers by district.  
- Religious composition of districts.  

### **Task 8: Interactive Streamlit Dashboard**  
Created an interactive dashboard to visualize census data insights.  

## **Setup Instructions**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/Census-Data-Analysis-Pipeline.git
   cd Census-Data-Analysis-Pipeline

