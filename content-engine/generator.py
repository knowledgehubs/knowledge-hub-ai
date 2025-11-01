import os, random, datetime

# Paths
keywords_dir = "content-engine/keywords/"
blocks_dir = "content-engine/blocks/"
posts_dir = "posts/"

# Load blocks
def load_blocks(folder):
    path = os.path.join(blocks_dir, folder)
    return [open(os.path.join(path, f)).read() for f in os.listdir(path) if f.endswith(".txt")]

blocks = {
    "openings": load_blocks("openings"),
    "introductions": load_blocks("introductions"),
    "explanations": load_blocks("explanations"),
    "advantages": load_blocks("advantages"),
    "limitations": load_blocks("limitations"),
    "steps": load_blocks("steps"),
    "comparisons": load_blocks("comparisons"),
    "tips": load_blocks("tips"),
    "cta": load_blocks("cta"),
}

# Generate post
def generate_post(keyword):
    today = datetime.date.today().isoformat()
    slug = keyword.replace(" ", "-")

    content = f"""# {keyword.title()}

{random.choice(blocks['openings'])}

{random.choice(blocks['introductions'])}

{random.choice(blocks['explanations'])}

### Benefits
{random.choice(blocks['advantages'])}

### Challenges
{random.choice(blocks['limitations'])}

### Step-by-step guide
{random.choice(blocks['steps'])}

### Comparison
{random.choice(blocks['comparisons'])}

### Practical Tips
{random.choice(blocks['tips'])}

---

{random.choice(blocks['cta'])}
"""

    filename = f"{today}-{slug}.md"
    filepath = os.path.join(posts_dir, filename)
    with open(filepath, "w") as f:
        f.write(content)

    print(f"✅ Generated: {filepath}")


# Process one keyword only each run
files = sorted([f for f in os.listdir(keywords_dir) if f.endswith(".md")])
if not files:
    print("🎉 No keywords left!")
    exit()

file = files[0]
keyword = open(os.path.join(keywords_dir, file)).read().replace("keyword:", "").strip()

generate_post(keyword)

# Remove keyword file after use
os.remove(os.path.join(keywords_dir, file))
print(f"🗑️ Used & removed: {file}")
