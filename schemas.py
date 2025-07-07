from pydantic import BaseModel, Field
# class ResponseFormatter(BaseModel):
#     """Always use this tool to structure your response to the user."""
#     answer: str = Field(description="The answer to the user's question")
#     followup_question: str = Field(description="A followup question the user could ask")


class ResponseFormatter(BaseModel):
    """Always use this tool to structure your response to the user."""
    # answer: str = Field(description="The answer to the user's question")
    # followup_question: str = Field(description="A followup question the user could ask")
    rationale: str = Field(description="A brief explanation of your reasoning for the next action")
    knowledge_gap: str = Field(description="A sentence stating the current knowledge gap")
    action: str = Field(description="The action to take next, one of ['search', 'visit', 'answer']")
    action_param: str = Field(description="The parameter for the action, e.g., a search query or a URL to visit or the final answer")