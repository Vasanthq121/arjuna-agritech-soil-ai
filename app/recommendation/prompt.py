import json


class RecommendationPrompt:

    @staticmethod
    def build(report, crop, rag_context):

        soil_json = report.model_dump()

        return f"""
You are an expert agronomist.

Crop:
{crop}

Validated Soil Report:
{json.dumps(soil_json, indent=2)}

Agronomy Knowledge:
{rag_context}

Generate ONLY valid JSON.

Return this schema:

{{
    "summary": "...",

    "recommendations":[
        {{
            "parameter":"",
            "status":"",
            "fertilizer":"",
            "dose":"",
            "application":"",
            "reason":"",
            "precaution":""
        }}
    ]
}}
"""