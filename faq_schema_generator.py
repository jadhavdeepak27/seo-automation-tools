import json

def generate_faq_schema(qa_pairs):
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    
    for question, answer in qa_pairs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer
            }
        })
    
    return json.dumps(schema, indent=4)

# Example Usage to show off in your Portfolio
qa_list = [
    ("What is SGE in SEO?", "Search Generative Experience is Google's AI-powered search results."),
    ("How to optimize for AI search?", "Focus on entity-based content and clear schema markup.")
]

print(generate_faq_schema(qa_list))
