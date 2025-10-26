# Sample Transcript

```
$ python -m multi_agentic.cli demo --message "The printer on floor 3 is jammed again."
{
  "history": [
    "HumanMessage(content='The printer on floor 3 is jammed again.', additional_kwargs={}, response_metadata={}, name='customer', id='')",
    "AIMessage(content='Customer reports: The printer on floor 3 is jammed again.', additional_kwargs={}, response_metadata={}, name='intake', id='')",
    "AIMessage(content='Matched FAQ: The printer is jammed. What should I do?\nConfidence: 0.73\nRecommended steps: Power off the printer, remove the paper tray, and gently clear the jam. Refer to the printer manual section 4.2 for diagrams.', additional_kwargs={}, response_metadata={}, name='knowledge', id='')",
    "AIMessage(content='Summary: Customer reports: The printer on floor 3 is jammed again.\n\nSolution:\nPower off the printer, remove the paper tray, and gently clear the jam. Refer to the printer manual section 4.2 for diagrams.\n\nLet us know if you need further assistance.', additional_kwargs={}, response_metadata={}, name='resolution', id='')"
  ],
  "customer_issue": "Customer reports: The printer on floor 3 is jammed again.",
  "proposed_solution": "Power off the printer, remove the paper tray, and gently clear the jam. Refer to the printer manual section 4.2 for diagrams.",
  "resolution": "Summary: Customer reports: The printer on floor 3 is jammed again.\n\nSolution:\nPower off the printer, remove the paper tray, and gently clear the jam. Refer to the printer manual section 4.2 for diagrams.\n\nLet us know if you need further assistance.",
  "finished": true
}
```
