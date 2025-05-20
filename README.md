# Ice Breaker

Ice Breaker is an automated tool that helps you "break the ice" with new contacts by generating a concise summary and interesting facts from their LinkedIn profile. The project leverages LLMs, web scraping, and search tools to find a person's LinkedIn profile, extract relevant data, and present it in an easy-to-digest format.

## Features

- **LinkedIn Profile Lookup:** Finds a person's LinkedIn profile using their name.
- **Profile Data Scraping:** Extracts key information from the LinkedIn profile.
- **Summary & Facts Generation:** Uses LLMs to generate a summary and a list of interesting facts.
- **API Access:** FastAPI backend to serve summary and facts via HTTP.
- **Streamlit Frontend:** Simple web interface for user input and displaying results.

## Project Structure

```
ice_breaker/
│
├── agent/                    # LinkedIn lookup agent logic
├── third_parties/            # LinkedIn scraping logic
├── tools/                    # Search tools
├── app.py                    # FastAPI backend
├── frontend.py               # Streamlit frontend
├── ice_breaker.py            # Main orchestration logic
├── .env                      # API keys and environment variables
├── README.md                 # Project documentation
└── ...
```

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kartheekakkur/ice_breaker.git
    cd ice_breaker
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Copy `.env.example` to `.env` and fill in your API keys for OpenAI, ScrapIn, and Tavily.

4. **Run the FastAPI backend:**
    ```bash
    uvicorn app:app --reload
    ```

5. **Run the Streamlit frontend:**
    ```bash
    streamlit run frontend.py
    ```

## Usage

1. Open the Streamlit app in your browser (usually at `http://localhost:8501`).
2. Enter the name of the person you want to "break the ice" with.
3. Click "Get Ice Breaker" to see a summary and interesting facts about them.

![image](https://github.com/user-attachments/assets/016b410c-32e3-4987-8a1b-44499c9f1394)


## API

- **GET /**  
  Returns a welcome message.

- **GET /ice_break/{name}**  
  Returns a JSON with `summary` and `facts` for the given name.

## Example Output

```json
{
  "summary_and_facts": {
    "summary": "Vasudev Kartheek A. is a skilled professional in Cloud Computing, Machine Learning, IoT, and Kubernetes...",
    "facts": [
      "Currently works as a Senior Site Reliability Engineer at SentinelOne since September 2022.",
      "Previously worked at SolarWinds, where he implemented code signing and automated Kubernetes deployments.",
      "...more facts..."
    ]
  }
}
```


*This project is for educational and demonstration purposes only. Please respect LinkedIn's terms of service and privacy policies.*
