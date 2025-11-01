import os, random, datetime, re

BLOCKS_DIR = "blocks"
POSTS_DIR = "posts"

def load_blocks(filename):
    path = os.path.join(BLOCKS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

blocks = {
    "hook": load_blocks("hooks.txt"),
    "intro": load_blocks("intros.txt"),
    "explain": load_blocks("explanations.txt"),
    "pros": load_blocks("pros.txt"),
    "cons": load_blocks("cons.txt"),
    "steps": load_blocks("steps.txt"),
    "compare": load_blocks("comparisons.txt"),
    "tips": load_blocks("tips.txt"),
    "cta": load_blocks("cta.txt"),
}

def generate_title():
    templates = [
        "What You Need to Know About {topic}",
        "A Complete Guide to {topic}",
        "Everything About {topic} Explained Simply",
        "{topic}: Pros, Cons & Best Practices",
        "Beginner Guide: Understanding {topic}",
        "{topic} — Full Breakdown & Tips",
    ]
    topic = random.choice([
        "Online Learning",
        "Skill Development",
        "Digital Courses",
        "Self-Education",
        "Remote Skills",
        "Personal Growth",
        "Career Upskilling"
    ])
    return random.choice(templates).format(topic=topic)

def create_post():
    title = generate_title()
    slug = re.sub(r'[^a-z0-9\-]', '', title.lower().replace(" ", "-"))
    filename = f"{datetime.date.today()}-{slug}.md"
    path = os.path.join(POSTS_DIR, filename)

    content = f"""---
title: "{title}"
date: {datetime.datetime.utcnow().isoformat()}
---

### {random.choice(blocks['hook'])}

{random.choice(blocks['intro'])}

## Explanation
{random.choice(blocks['explain'])}

## Pros
{random.choice(blocks['pros'])}

## Cons
{random.choice(blocks['cons'])}

## Steps
{random.choice(blocks['steps'])}

## Comparison
{random.choice(blocks['compare'])}

## Tips
{random.choice(blocks['tips'])}

## Final Thoughts
{random.choice(blocks['cta'])}
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Generated: {filename}")

if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# Generate 5 posts every run (first test)
for _ in range(5):
    create_post()
