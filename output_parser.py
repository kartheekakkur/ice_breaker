from typing import Any, Dict, List
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Summary(BaseModel):
    """
    This class is used to parse the output of the LLM.
    """
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="The interesting facts about the person.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Pydantic model to a dictionary.
        """
        return {
            "summary": self.summary,
            "facts": self.facts
        }



summary_parser = PydanticOutputParser(pydantic_object=Summary)