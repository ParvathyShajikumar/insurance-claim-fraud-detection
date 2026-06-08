````markdown
# 🏥 GenAI-Powered Insurance Claim Fraud Detection System

An AI-powered insurance claim duplicate and fraud detection application built using:

- Python
- Streamlit
- Claude API (Anthropic)
- Fuzzy Matching
- Fixed-width file parsing

The application detects:
- Exact duplicate claims
- Fuzzy duplicate claims
- Suspicious fraud patterns
- Invalid insurance claim records

---

# 🚀 Features

✅ Fixed-width insurance claim file parsing  
✅ Record validation layer  
✅ Fuzzy duplicate detection  
✅ Similarity scoring  
✅ AI-powered fraud analysis using Claude  
✅ Interactive Streamlit dashboard  
✅ Downloadable fraud reports  
✅ Invalid record identification  
✅ Explainable fraud indicators  

---

# 🧠 Project Architecture

```text
Insurance Claim File
        ↓
Fixed-width Parser
        ↓
Validation Layer
        ↓
Duplicate Detection
        ↓
Fuzzy Matching
        ↓
Claude AI Fraud Analysis
        ↓
Fraud Dashboard (Streamlit)
````

***

# 📂 Project Structure

```text
insurance-claim-ai/
│
├── data/
│   └── data.txt
│
├── output/
│   ├── output.json
│   └── invalid_records.json
│
├── parser.py
├── validator.py
├── utils.py
├── duplicate_detector.py
├── ai_analysis.py
├── app.py
├── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

***

# 🛠️ Tech Stack

* Python 3
* Streamlit
* Anthropic Claude API
* Python dotenv
* difflib (fuzzy matching)

***

# 📄 Input File Format

The application processes fixed-width insurance claim files.

## Sample Record

```text
0000001001Ravi Kumar                 20240501Aster Hospital             000050000POL000001
```

## Field Mapping

| Field          | Start | End |
| -------------- | ----- | --- |
| claim_id       | 0     | 10  |
| customer_name  | 10    | 38  |
| claim_date     | 38    | 46  |
| hospital       | 46    | 74  |
| amount         | 74    | 83  |
| policy_number  | 83    | 106 |

***

# 🔍 Duplicate Detection Logic

The system uses hybrid duplicate detection:

## Rule-Based Validation

* Same policy number
* Same/similar claim amount
* Similar customer names
* Similar hospital names

***

## Fuzzy Matching

Uses similarity scoring:

```python
SequenceMatcher().ratio()
```

Example:

```text
Ravi Kumar ↔ R Kumar
Aster Hospital ↔ Aster Medcity
```

***

## AI-Based Fraud Analysis

Claude AI analyzes suspicious claims and determines:

* Duplicate claim status
* Possible fraud
* Fraud indicators
* Recommended action

***

# 🧠 Example AI Output

```json
{
  "duplicate_claim": true,
  "possible_fraud": true,
  "fraud_indicators": [
    "Same policy number",
    "Identical claim amount",
    "Similar customer names"
  ],
  "recommended_action": "Investigate immediately"
}
```

***

# ▶️ Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd insurance-claim-ai
```

***

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

***

## 3. Configure Environment Variables

Create `.env`

```env
ANTHROPIC_API_KEY=your_api_key_here
```

***

# ▶️ Run Application

## Run Streamlit UI

```bash
streamlit run app.py
```

***

# 📊 Dashboard Features

The Streamlit dashboard provides:

✅ Duplicate claim count  
✅ Invalid record count  
✅ AI fraud insights  
✅ Similarity scores  
✅ Fraud indicators  
✅ Recommended actions

***

# ✅ Example Fraud Scenarios

## Exact Duplicate

* Same customer
* Same amount
* Same date
* Different claim IDs

→ Duplicate Claim = TRUE

***

## Suspicious Fraud

* Same policy number
* Different customer names
* Similar hospital
* Similar amount

→ Possible Fraud = TRUE

***

# 🔐 Security

API keys are stored securely using `.env`

Never commit:

* `.env`
* API keys
* credentials

***

# 📦 requirements.txt

```text
anthropic
streamlit
python-dotenv
```

***

# 🚀 Future Enhancements

* Batch processing for large files
* Async Claude API calls
* Risk scoring engine
* Fraud analytics dashboard
* Database integration
* RAG-powered insurance policy validation
* User authentication

***

# 🏆 Key Learnings

This project demonstrates:

✅ Hybrid AI architecture  
✅ GenAI integration  
✅ Data engineering workflows  
✅ Explainable AI  
✅ Fraud detection systems  
✅ Enterprise validation patterns

***

# 👨‍💻 Author

Built as a hands-on GenAI engineering project focused on insurance claim fraud detection and duplicate analysis.

```
```
