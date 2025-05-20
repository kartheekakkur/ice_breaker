from fastapi import FastAPI

from ice_breaker import ice_break_with


app = FastAPI()

@app.get("/")
def read_root():
    return {"ICE_BREAKER": "Welcome to the Ice Breaker API!"}
@app.get("/ice_break/{name}")
def get_user(name: str):
    """
    Ice Breaker API endpoint to get LinkedIn profile summary and facts.
    """
    # Use the 'name' parameter directly as it comes from the path
    user_summary = ice_break_with(name)
    return {"summary_and_facts": user_summary.to_dict()}
