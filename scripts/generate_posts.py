import os, random, datetime, json, glob, re

# ==== Load Config ====
with open("config.json", "r") as f:
    cfg = json.load(f)

# ==== Paths ====
BLOCKS_DIR = "blocks"
POSTS_DIR = "posts"
DATA_DIR = "data"
HEADERS_DIR = f"{DATA_DIR}/headers"

# Load affiliate links
try:
    with open(f"{DATA_DIR}/affiliate_links.txt") as f:
        affiliate_links = [x.strip() for x in f.readlines() if x.strip()]
except:
    affiliate_links = ["https://your-affiliate-link.com"]

# Load headers
def load_file(path):
    if os.path.exists(path):
        with open(path) as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    return []

h2_headers = load_file(f"{HEADERS_DIR}/h2_headers.txt")
h3_headers = load_file(f"{HEADERS_DIR}/h3_headers.txt")

# ==== Generate Article ====
def generate_article():
    num_blocks = random.randint(cfg["min_blocks"], cfg["max_blocks"])
    selected_blocks = []

    for folder in glob.glob(f"{BLOCKS_DIR}/*"):
        files = os.listdir(folder)
        if files:
            chosen = random.choice(files)
            selected_blocks.append(open(f"{folder}/{chosen}").read().strip())
            if len(selected_blocks) >= num_blocks:
                break

    article = ""

    # Add H2 title
    if cfg["include_h2"] and h2_headers:
        article += f"## {random.choice(h2_headers)}\n\n"

    # Add blocks
    for block in selected_blocks:
        article += block + "\n\n"

        # Add H3 occasionally
        if cfg["include_h3"] and h3_headers and random.random() > 0.6:
            article += f"### {random.choice(h3_headers)}\n\n"

    # Add CTA + affiliate link
    affiliate = random.choice(affiliate_links)
    article += f"\n\n> 👉 **Learn More Here:** [{affiliate}]({affiliate})\n\n"

    return article

# ==== Save Posts for Today ====
today = datetime.date.today().strftime("%Y-%m-%d")

for i in range(cfg["daily_articles"]):
    title = f"{today}-ai-insight-{i}.md"
    path = f"{POSTS_DIR}/{title}"
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(generate_article())

print("✅ Articles Generated!")
