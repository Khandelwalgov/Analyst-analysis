from flask import Flask, render_template,request
import datetime
import pandas as pd
app = Flask(__name__)

l1=['Enkei Wheels (India)..', 'L&T Finance Ltd.', 'Parekh Aluminex Ltd.', 'Heubach Colorants In..', 'Sintex Industries Ltd.', 'Shriram Finance Ltd.', 'Gammon India Ltd.', 'Kalpataru Projects I..', 'MindTree Ltd.', 'Dewan Housing Financ..', 'LT Foods Ltd.', 'AGI Greenpac Ltd.', 'Dishman Pharmaceutic..', 'Lakshmi Vilas Bank L..', 'Brokerage Research R..', 'Automobiles & Auto C..', 'Crude Oil', 'Allahabad Bank [Merg..', 'Samvardhana Motherso..', 'World Economy and Ma..', 'India Macro Indicators', 'Hariom Pipe Industri..', 'Delhivery Ltd.', 'Fairchem Organics Ltd.', 'Medplus Health Servi..', 'Welspun Living Ltd.', 'Privi Speciality Che..', 'Berger Paints (India..', 'ZF Commercial Vehicl..', 'Sterlite Technologie..', 'GRUH Finance Ltd.', 'Lanco Infratech Ltd.', 'Hexaware Technologie..', 'Corporation Bank [Me..', 'ING Vysya Bank Limited', 'Cairn India Limited', 'Aditya Birla Nuvo Li..', 'Ion Exchange (India)..', 'Dalmia Bharat Ltd.', 'UCAL Ltd.', 'Srikalahasthi Pipes ..', 'Syndicate Bank [Merg..', 'Market Movement', 'Technology trends', 'Gujarat Borosil Ltd.', 'Gateway Distriparks ..', 'GlaxoSmithKline Cons..', 'Dalmia Bharat Ltd.(O..', 'Shriram City Union F..', '360 One Wam Ltd.', 'Hindware Home Innova..', 'Hitachi Energy India..', 'Simmonds Marshall Ltd.', 'Easy Trip Planners L..', 'Shriram Properties L..', 'Fermenta Biotech Ltd.', 'SBI Home Finance Ltd.', 'Tata Steel Long Prod..', 'Bharat Financial Inc..', 'Star Ferro and Cemen..', 'Rubfila Internationa..', 'Kirloskar Pneumatic ..', 'International Travel..', 'GMR Airports Infrast..', 'Gloster Ltd.[Old]', 'South East Agro Indu..', 'Automobile Corporati..', 'Meghmani Organics Lt..', 'Geometric Limited', 'Deep Energy Resource..', 'Cosmo First Ltd.', '3B BlackBio Dx Ltd.', 'Beta Drugs Ltd.', 'Jeena Sikho Lifecare..', 'Kwality Ltd.', 'One97 Communications..', 'Go Fashion (India) L..', 'Consumer Durables', 'Prabhat Dairy Ltd.', 'Garware Hi-Tech Film..', 'Jio Financial Servic..', 'International Homete..', 'Natural Vanaspati Ltd.', 'Prudential Sugar Cor..', 'Personal Finance & I..', 'Shelter Infra Projec..', 'Mutual Funds News', 'India Policy and Ref..', 'Asian Energy Service..', 'Jeevan Scientific Te..', 'Polaris Consulting &..', 'Advanta Limited', 'Oriental Bank of Com..', 'Trading Strategy', 'Oil and Gas', 'Rupee and Forex Move..', 'Banks', 'Commodities', 'Marico Kaya Enterpri..', 'Data Patterns (India..', 'Patanjali Foods Ltd.', 'Azad Engineering Ltd.', 'ASK Automotive Ltd.', 'Nexus Select Trust R..', 'Vijaya Diagnostic Ce..', 'PB Fintech Ltd.', 'Investment & Precisi..', 'NGL Fine - Chem Ltd.', 'Gold and Precious Me..', 'Veer Energy & Infras..', 'Medi Assist Healthca..', 'Jupiter Wagons Ltd.', 'Anand Rathi Wealth L..', 'Orient Tradelink Ltd.', 'Oriental Remedies & ..', 'Kriti Industries (In..', 'Ashapura Intimates F..', 'Viaan Industries Ltd.', 'Kesar Petroproducts ..', 'RCI Industries & Tec..', 'Pennar Engineered Bu..', 'Johnson Controls-Hit..', 'Simplex Projects Ltd.', 'Elin Electronics Ltd.', 'Hampton Sky Realty L..', 'Baid Finserv Ltd.', 'Radhika Jeweltech Ltd.', 'Tiger Logistics (Ind..', 'DCX Systems Ltd.', 'Ganesh Benzoplast Ltd.', 'Happy Forgings Ltd.', 'Steel Cast Ltd.', 'Fast Track Entertain..', 'Sandur Manganese & I..', 'GCV Services Ltd.', 'BSE Sensex', 'United Breweries (Ho..', 'Hinduja Foundries Li..', 'Monsanto India Ltd.', 'Anuh Pharma Ltd.', 'Software & Services', 'Pharmaceuticals & Bi..', 'Capital Goods', 'Metal and Mining', 'United Bank of India..', 'Divgi Torqtransfer S..', 'Environment', 'Punjab Fibres Ltd.', 'Ranbaxy Laboratories..', 'DFM Foods Ltd.', 'Stovec Industries Ltd.', 'Pondy Oxides & Chemi..', 'Veljan Denison Ltd.', 'Pakka Ltd.', 'Excel Crop Care Ltd.', 'Adani Energy Solutio..', 'Sadhana Nitro Chem L..', 'Sai Silks (Kalamandi..', 'Lloyds Engineering W..', 'Welspun Specialty So..', 'Lloyds Metals & Ener..', 'Black Box Ltd.', 'Sunil Hitech Enginee..', 'Vijaya Bank']

df1=pd.read_csv(r'E:\python\CompleteScrapedData.csv')
history=pd.read_csv(r'E:\python\HistoricDataWithCompanyAgain.csv')

def convert_date(date_str):
    # Define a dictionary to map month abbreviations to their numerical values
    month_map = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    
    # Check if the date string is in "08 Apr 2024" format
    if date_str[2] == ' ':
        # Split the date string into its components
        parts = date_str.split()
        
        # Extract day, month (convert from abbreviation to number), and year
        day = int(parts[0])
        month = month_map[parts[1]]
        year = int(parts[2])
    
    # Check if the date string is in "2020-04-03" format
    elif date_str[4] == '-':
        # Split the date string into its components
        parts = date_str.split('-')
        
        # Extract year, month, and day
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    
        
    return datetime.date(year,month,day)

#PreProcessing
df1['Date'] = df1['Date'].apply(convert_date)
history['Date'] = history['Date'].apply(convert_date)
unique_analysts = df1['Analyst'].unique()

# Create a dictionary to store smaller DataFrames for each analyst
analyst_dfs = {}

# Iterate over each unique analyst
for analyst in unique_analysts:
    # Filter the original DataFrame for rows where the 'Analyst' column matches the current analyst
    analyst_df = df1[df1['Analyst'] == analyst]
    # Add the filtered DataFrame to the dictionary
    analyst_df.reset_index(drop=True, inplace=True)
    analyst_dfs[analyst] = analyst_df
unique_history = history['Company'].unique()

# Create a dictionary to store smaller DataFrames for each company
company_data = {company: df.reset_index(drop=True) for company, df in history.groupby('Company')}


@app.route('/')
def index():
    #final_df = process_data()
    return render_template('index.html')
@app.route('/generate_data', methods=['POST'])
def generate_data():
    if request.method == 'POST':
        start_date = convert_date(request.form['start-date'])
        end_date = convert_date(request.form['end-date'])
        dur = request.form['period']
        if dur=="1Y":
            x = datetime.timedelta(days=365)
        elif dur=="6M":
            x = datetime.timedelta(days=182)
        elif dur=="3M":
            x= datetime.timedelta(days=91)
        print(start_date,end_date,x)
        analyst_to_be_displayed= "All"

        to_be_processed=[]
        calls_to_be_processed={}

        if analyst_to_be_displayed=='All':
            to_be_processed=list(analyst_dfs.keys())
        else:
            to_be_processed =[analyst_to_be_displayed]

        final_dict = {}

        for broker in analyst_dfs:
            if broker in to_be_processed:
                if start_date < analyst_dfs[broker]['Date'].iloc[-1]:
                    if end_date >= analyst_dfs[broker]['Date'].iloc[-1]:
                        filtered_df = analyst_dfs[broker][
                            (analyst_dfs[broker]['Date'] >= start_date) & (analyst_dfs[broker]['Date'] <= end_date) & (
                                ~analyst_dfs[broker]['Company'].isin(l1))]
                        calls_to_be_processed[broker] = filtered_df
                        # Put a warning, date set earlier, data starts from {analst_dfs[broker]['Date'][-1]}
                    else:
                        continue
                        # No Data to be processed between the set dates!
                else:

                    filtered_df = analyst_dfs[broker][
                        (analyst_dfs[broker]['Date'] >= start_date) & (analyst_dfs[broker]['Date'] <= end_date) & (
                            ~analyst_dfs[broker]['Company'].isin(l1))]
                    calls_to_be_processed[broker] = filtered_df

        for broker in calls_to_be_processed:
            bdf = calls_to_be_processed[broker]
            calls = 0
            successes = 0
            for tar, adv, dat, com in zip(bdf['Target'], bdf['Advice'], bdf['Date'], bdf['Company']):

                call_date = dat
                till_date = call_date + x
                if company_data[com]['Date'].iloc[-1] < till_date:
                    continue
                calls += 1
                if adv in ['Buy', 'Neutral', 'Hold', 'Accumulate']:
                    reach = company_data[com]['High'][
                        (company_data[com]['Date'] >= call_date) & (company_data[com]['Date'] <= till_date)].max()
                else:
                    reach = company_data[com]['Low'][
                        (company_data[com]['Date'] >= call_date) & (company_data[com]['Date'] <= till_date)].min()

                    # Check if reach and tar are valid numeric values before comparison
                if reach is not None and not pd.isna(reach) and not pd.isna(tar):
                    if adv in ['Buy', 'Neutral', 'Hold', 'Accumulate']:
                        if reach >= tar:
                            successes += 1
                    else:
                        if reach <= tar:
                            successes += 1

                    # Calculate success percentage
                percent = (successes / calls) * 100 if calls != 0 else 0
                percentage = f"{percent:.2f}%"  # Format percentage to two decimal places
            final_dict[broker] = {"Total Calls in Period: ": calls, "Total Successes in the period: ": successes,
                                "Success %": percentage}

        final_df = pd.DataFrame.from_dict(final_dict, orient='index')
        return render_template('index.html', df=final_df.to_html(classes='table table-striped'))

if __name__ == "__main__":
    app.run(debug=True)
