import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. TRAIN THE BRAIN (Fixed: 4 data points matched with 4 column names)
# Features: [Billed, Is_Psych_DX, Is_Psych_Prov] + Target: [Action]
train_data = [
    [5000, 1, 1, 1], 
    [100, 1, 0, 0], 
    [2000, 1, 1, 1], 
    [300, 0, 0, 0]
]
# We name all 4 columns here to stop the ValueError
training_df = pd.DataFrame(train_data, columns=['billed', 'is_f', 'is_psych', 'target'])

X_train = training_df[['billed', 'is_f', 'is_psych']]
y_train = training_df['target']

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 2. LOAD YOUR EXCEL DATA
file_name = 'Behaviorl health claims/claims_data.xlsx'

try:
    # Read the Excel sheet
    df_excel = pd.read_excel(file_name)
    
    # Make sure your Excel headers are lowercase to match the code below
    # Or we can force them to lowercase:
    df_excel.columns = [c.lower().strip() for c in df_excel.columns]

    print("\n" + "="*85)
    print(f"📂 LOADING DATA FROM: {file_name}")
    print("🧠 BHARATH'S BEHAVIORAL HEALTH (BH) BATCH PROCESSOR v5.1")
    print("="*85)
    print(f"{'CLAIM ID':<15} | {'DX CODE':<8} | {'BILLED':<8} | {'ALLOWED':<8} | {'AI PREDICTION'}")
    print("-" * 85)

    for index, row in df_excel.iterrows():
        c_id = row['claim id']
        
        # --- NEW CLEANING LOGIC START ---
        # This removes '$' and ',' so '$10,000' becomes 10000.0
        raw_billed = str(row['billed charges'])
        billed = float(raw_billed.replace('$', '').replace(',', ''))
        
        raw_allowed = str(row['allowed amount'])
        allowed = float(raw_allowed.replace('$', '').replace(',', ''))
        # --- NEW CLEANING LOGIC END ---

        dx = str(row['diagnosis code'])
        prov = 1 if "psych" in str(row['provider type']).lower() else 0

        is_f = 1 if dx.upper().startswith('F') else 0
        
        check = pd.DataFrame([[billed, is_f, prov]], columns=['billed', 'is_f', 'is_psych'])
        prediction = model.predict(check)
        
        if prediction[0] == 1:
            status = "🚩 PEND: Route to BH Team"
        else:
            status = "✅ ALLOW: Auto-Process"
            
        # FIXED: Cleaned up the print line and removed the break
        print(f"{str(c_id):<15} | {dx:<8} | ${billed:<7.0f} | ${allowed:<7.0f} | {status}")

    print("="*85)

except FileNotFoundError:
    print(f"❌ ERROR: '{file_name}' not found. Check the folder path.")
except Exception as e:
    print(f"❌ AN ERROR OCCURRED: {e}")