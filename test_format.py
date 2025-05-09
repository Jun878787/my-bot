import re
from datetime import datetime

def parse_date(date_str):
    today = datetime.now()
    
    if '/' in date_str:
        month, day = map(int, date_str.split('/'))
        return f"{today.year}-{month:02d}-{day:02d}"
    elif '-' in date_str and date_str.count('-') == 1:  # For MM-DD format
        month, day = map(int, date_str.split('-'))
        return f"{today.year}-{month:02d}-{day:02d}"
    elif '.' in date_str:  # For MM.DD format
        month, day = map(int, date_str.split('.'))
        return f"{today.year}-{month:02d}-{day:02d}"
    else:
        return today.strftime('%Y-%m-%d')

# Test format matching
test_inputs = [
    "5/01 TW+10000",  # Basic format
    "5/01 TW-1000",   # Negative amount
    "5/01 CN+500",    # CN currency
    "5/01 CN-200",    # CN negative
    "05/01 TW+10000", # Leading zero
    " 5/01 TW+10000 ", # With spaces
    "5/1 TW+10000",   # Single digit day
    "TW+10000",       # No date
    "5-01 TW+10000",  # Using dash
    "5.01 TW+10000",  # Using dot
]

print("==== Testing Standard Pattern ====")
for input_text in test_inputs:
    pattern = r'^\s*(\d{1,2}/\d{1,2})\s+(TW|CN)([+\-])\s*(\d+(\.\d+)?)\s*$'
    match = re.match(pattern, input_text)
    if match:
        print(f"Input: {input_text} - MATCHED")
    else:
        print(f"Input: {input_text} - NO MATCH")

print("\n==== Testing Flexible Pattern ====")
for input_text in test_inputs:
    # More flexible pattern to handle different date separators
    flexible_pattern = r'^\s*(\d{1,2}[/\-\.]\d{1,2})\s+(TW|CN)([+\-])\s*(\d+(\.\d+)?)\s*$'
    match = re.match(flexible_pattern, input_text)
    if match:
        date_str = match.group(1)
        currency = match.group(2)
        op = match.group(3)
        amount = float(match.group(4))
        
        if op == '-':
            amount = -amount
        
        try:
            date = parse_date(date_str)
            date_display = datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d')
            
            print(f"Input: {input_text}")
            print(f"  Match: date={date_str}, currency={currency}, op={op}, amount={amount}")
            print(f"  Parsed: date={date}, display={date_display}, amount={amount}")
        except Exception as e:
            print(f"Input: {input_text} - Error parsing: {str(e)}")
    else:
        print(f"Input: {input_text} - NO MATCH")

print("\n==== Testing Date Parsing ====")
dates = ["5/01", "5/1", "05/01", "5-01", "5.01"]
for date_str in dates:
    try:
        parsed = parse_date(date_str)
        formatted = datetime.strptime(parsed, '%Y-%m-%d').strftime('%m/%d')
        print(f"Date {date_str} parsed as: {parsed}, formatted as: {formatted}")
    except Exception as e:
        print(f"Error processing date {date_str}: {str(e)}") 