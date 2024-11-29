import json
import requests

Debug = False
Authorization = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

def get_guest_token():
    url = "https://api.x.com/1.1/guest/activate.json"
    res = requests.post(url, headers={
        "Authorization": Authorization
    })
    if res.status_code == 200:
        res_data = res.json()
        print(res_data, res_data["guest_token"])
        if "guest_token" in res_data:
            return res_data["guest_token"]
    else:
        raise Exception(f"get_guest_token() fail! status_code:{res.status_code}")

def get_post_detail(link: str):
    status = link.split("/")[-1]
    url = f"https://api.x.com/graphql/OoJd6A50cv8GsifjoOHGfg/TweetResultByRestId?variables=%7B%22tweetId%22%3A%22{status}%22%2C%22withCommunity%22%3Afalse%2C%22includePromotedContent%22%3Afalse%2C%22withVoice%22%3Afalse%7D&features=%7B%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticleRichContentState%22%3Atrue%2C%22withArticlePlainText%22%3Afalse%2C%22withGrokAnalyze%22%3Afalse%2C%22withDisallowedReplyControls%22%3Afalse%7D"
    # url = f"https://x.com/i/api/graphql/nBS-WpgA6ZG0CyNHD517JQ/TweetDetail?variables=%7B%22focalTweetId%22%3A%22{status}%22%2C%22with_rux_injections%22%3Afalse%2C%22rankingMode%22%3A%22Relevance%22%2C%22includePromotedContent%22%3Atrue%2C%22withCommunity%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withBirdwatchNotes%22%3Atrue%2C%22withVoice%22%3Atrue%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticleRichContentState%22%3Atrue%2C%22withArticlePlainText%22%3Afalse%2C%22withGrokAnalyze%22%3Afalse%2C%22withDisallowedReplyControls%22%3Afalse%7D"
    
    res = requests.get(url, headers={
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': '1862387677276053540',
        'Cookie': 'guest_id=v1%3A173267282735050314; guest_id_ads=v1%3A173267282735050314; guest_id_marketing=v1%3A173267282735050314; personalization_id="v1_sEfgk8VC8aznCtrW+AT4Ug=="'
    })
    
    if res.status_code == 200:
        response_data = res.json()
        if Debug:
            with open(f'./debug/{status}.json', 'w', encoding='utf-8') as json_file:
                json.dump(response_data, json_file, ensure_ascii=False, indent=4)
        parse_data = parse_post_detail(response_data)
        parse_data["link"] = link
        parse_data["t_id"] = status
        if Debug:
            with open(f'./debug/{status}_parse.json', 'w', encoding='utf-8') as json_file:
                json.dump(parse_data, json_file, ensure_ascii=False, indent=4)
            print(parse_data["text"])
        return parse_data
    else:
        print(f"request fail! status_code:{res.status_code}")
        

def parse_post_detail(data):
    result = data["data"]["tweetResult"]["result"]
    user_id = result["core"]["user_results"]["result"]["rest_id"]
    name = result["core"]["user_results"]["result"]["legacy"]["name"]
    handle = result["core"]["user_results"]["result"]["legacy"]["screen_name"]
    avatar = result["core"]["user_results"]["result"]["legacy"]["profile_image_url_https"]
    content = result["legacy"]["full_text"]
    favorite_count = result["legacy"]["favorite_count"]
    quote_count = result["legacy"]["quote_count"]
    reply_count = result["legacy"]["reply_count"]
    retweet_count = result["legacy"]["retweet_count"]
    create_time = result["legacy"]["created_at"]
    
    hashtags = []
    if "hashtags" in result["legacy"]["entities"]:
        for item in result["legacy"]["entities"]["hashtags"]:
            hashtags.append(item["text"])
            
    
    media = []
    if "media" in result["legacy"]["entities"]:
        for item in result["legacy"]["entities"]["media"]:
            if item["type"] == "photo":
                media.append({
                    "type": "photo",
                    "url": item["media_url_https"],
                    "sizes": item["sizes"]
                })
            elif item["type"] == "video":
                media.append({
                    "type": "video",
                    "video_info": item["video_info"]["variants"],
                    "cover_img": item["media_url_https"],
                    "sizes": item["sizes"]
                })
            else:
                raise(f"Unknow media type:{item['type']} when parse post detail!")
            
                
    text = f'user_id:{user_id} \n name:{name} \n handle:@{handle} \n avatar:{avatar} \n content:{content} \n create_time:{create_time} \n media:{media}'
    payload = {
        "tu_id": user_id,
        "nickname": name,
        "handle": "@"+handle,
        "avatar": avatar,
        "content": content,
        "favorite_count": favorite_count,
        "quote_count": quote_count,
        "reply_count": reply_count,
        "retweet_count": retweet_count,
        "create_time": create_time,
        "media": media,
        "text": text,
    }
    return payload

def test():
    url = "https://api.x.com/graphql/OoJd6A50cv8GsifjoOHGfg/TweetResultByRestId?variables=%7B%22tweetId%22%3A%221861953112296067128%22%2C%22withCommunity%22%3Afalse%2C%22includePromotedContent%22%3Afalse%2C%22withVoice%22%3Afalse%7D&features=%7B%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticleRichContentState%22%3Atrue%2C%22withArticlePlainText%22%3Afalse%2C%22withGrokAnalyze%22%3Afalse%2C%22withDisallowedReplyControls%22%3Afalse%7D"

    payload = {}
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': '1862387677276053540',
        'Cookie': 'guest_id=v1%3A173267282735050314; guest_id_ads=v1%3A173267282735050314; guest_id_marketing=v1%3A173267282735050314; personalization_id="v1_sEfgk8VC8aznCtrW+AT4Ug=="'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

if __name__ == "__main__":
    # url = "https://x.com/RemoteWLB/status/1852967973457399884"
    url = "https://x.com/Rothmus/status/1861953112296067128"
    get_post_detail(url)