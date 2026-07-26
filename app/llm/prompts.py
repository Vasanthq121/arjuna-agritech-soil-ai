SOIL_EXTRACTION_PROMPT = """
You are an expert agricultural AI.

Extract every soil parameter from the report.

Return ONLY valid JSON.

Schema:

{{
  "farmer_name": "",
  "sample_id": "",
  "crop": "",
  "location": "",
  "sample_date": "",
  "report_date": "",
  "parameters": [
    {{
      "parameter": "",
      "value": "",
      "unit": "",
      "rating": "",
      "remark": ""
    }}
  ]
}}

Report:

{report}
"""