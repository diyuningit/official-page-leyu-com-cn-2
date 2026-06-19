import json


# 内置站点信息列表
SITES = [
    {
        "name": "乐鱼体育",
        "url": "https://official-page-leyu.com.cn",
        "tags": ["体育", "娱乐", "在线平台"],
        "description": "乐鱼体育是一家专注于体育赛事与在线娱乐的综合平台，提供丰富的体育资讯和互动服务。",
        "keywords": ["乐鱼体育", "体育赛事", "在线娱乐"]
    },
    {
        "name": "示例资讯站",
        "url": "https://example-news.com",
        "tags": ["新闻", "资讯", "科技"],
        "description": "一个模拟的资讯站点，展示各类科技与行业动态。",
        "keywords": ["新闻", "科技资讯", "行业动态"]
    },
    {
        "name": "开发者社区",
        "url": "https://dev-community.io",
        "tags": ["开发者", "社区", "编程"],
        "description": "开发者交流与学习平台，汇聚各类技术文章与开源项目。",
        "keywords": ["开发者", "编程", "开源"]
    }
]


def format_site_summary(site):
    """
    格式化单个站点的摘要信息
    :param site: dict，包含站点名称、URL、标签、描述和关键词
    :return: str，结构化摘要字符串
    """
    name = site.get("name", "未知站点")
    url = site.get("url", "#")
    tags = site.get("tags", [])
    desc = site.get("description", "暂无描述")
    keywords = site.get("keywords", [])

    tag_str = ", ".join(tags)
    kw_str = ", ".join(keywords)

    summary_lines = [
        f"站点名称: {name}",
        f"访问地址: {url}",
        f"标签分类: {tag_str}",
        f"关键词: {kw_str}",
        f"简短说明: {desc}",
        "---"
    ]
    return "\n".join(summary_lines)


def generate_all_summaries(sites_list):
    """
    生成所有内置站点的摘要列表
    :param sites_list: list[dict]
    :return: list[str]
    """
    summaries = []
    for site in sites_list:
        summary = format_site_summary(site)
        summaries.append(summary)
    return summaries


def export_summaries_to_json(summaries):
    """
    将摘要列表导出为JSON格式字符串
    :param summaries: list[str]
    :return: str
    """
    data = {
        "total": len(summaries),
        "summaries": summaries
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def main():
    print("===== 站点摘要生成器 =====")
    print(f"共加载 {len(SITES)} 个内置站点\n")

    summaries = generate_all_summaries(SITES)

    print("结构化摘要输出:")
    for idx, summary in enumerate(summaries, 1):
        print(f"站点 {idx}:")
        print(summary)

    json_output = export_summaries_to_json(summaries)
    print("\nJSON 格式导出:")
    print(json_output)


if __name__ == "__main__":
    main()