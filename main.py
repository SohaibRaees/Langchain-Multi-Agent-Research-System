# from src.tools.tools import web_search,scrape_url

# result = web_search.invoke("latest advancements in AI")


# print(result)


from src.pipeline.pipeline import run_research_pipeline


topic = "The impact of AI on the job market in 2026"
run_research_pipeline(topic)