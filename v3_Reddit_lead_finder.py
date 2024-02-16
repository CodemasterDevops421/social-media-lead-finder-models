from v1_subreddits_finder import stage_3_final
from v1_subreddit_scanner import stage_4_scrape_posts
from V2_post_search.v2_post_search import v2_post_search
from V2_post_search.embedding_module import embed_and_upsert_to_pinecone


# This combines all of the other methods of the V3 reddit lead finder. Scrapes subreddits, uses GPT to analyse them, then returns the leads that match.
def v3_reddit_lead_finder(product_description, user_id_index_name) : 
    url_array = stage_3_final(product_description=product_description)
    scraped_posts = stage_4_scrape_posts(url_array)
    embed_and_upsert_to_pinecone(scraped_posts, user_id_index_name)
    final_leads = v2_post_search(product_description, user_id_index_name)
    return final_leads


test_product_description = """ 'My startup aims to allow users to type in the problem that their product is supposed to solve, and then from this it searches multiple social media platforms and then returns to the user the leads that have posted/commented about their problem'"""
test_user_id = "test-index"
v3_reddit_lead_finder(test_product_description, test_user_id)