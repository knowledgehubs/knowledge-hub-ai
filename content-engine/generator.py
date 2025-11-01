import os, random, datetime

# Paths
keywords_dir = "content-engine/keywords/"
blocks_dir = "blocks/"
posts_dir = "posts/"

# Load blocks file (each line or paragraph = 1 block)
def load_blocks(file_name):
    file_path = os.path.join(blocks_dir, file_name)
    if not os.path.exists(file_path):
        print(f"⚠️ Missing block file: {file_name}")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    # Split by double newline or newline
    return [p.strip() for p in content.split("\n\n") if p.strip()]

blocks = {
    "openings": load_blocks("hooks.txt"),
    "introductions": load_blocks("intros.txt"),
    "explanations": load_blocks("explanations.txt"),
    "advantages": load_blocks("pros.txt"),
    "limitations": load_blocks("cons.txt"),
    "steps": load_blocks("steps.txt"),
    "comparisons": load_blocks("comparisons.txt"),
    "tips": load_blocks("tips.txt"),
    "cta": load_blocks("cta.txt"),
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
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Generated: {filepath}")

# Process one keyword only each run
files = sorted([f for f in os.listdir(keywords_dir) if f.endswith(".md")])
if not files:
    print("🎉 No keywords left!")
    exit()

file = files[0]
keyword = open(os.path.join(keywords_dir, file), encoding="utf-8").read().replace("keyword:", "").strip()

generate_post(keyword)

# Remove keyword file after use
os.remove(os.path.join(keywords_dir, file))
print(f"🗑️ Used & removed: {file}")
