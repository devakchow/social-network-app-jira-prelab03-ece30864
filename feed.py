import datetime
import time
import clk

# --- PLACEHOLDER DUMMY DATA ---
# Simulating a database of social media posts
DUMMY_FEED = [
    {
        "id": 1,
        "username": "travel_bug",
        "content": "Just landed in Tokyo! The neon lights are absolutely mesmerizing. 🗼✨",
        "timestamp": "2 mins ago",
        "likes": 142,
        "comments": ["Jealous!", "Have an amazing trip!"]
    },
    {
        "id": 2,
        "username": "tech_guru",
        "content": "Writing clean code is like writing good poetry. Discuss. 💻📝",
        "timestamp": "15 mins ago",
        "likes": 89,
        "comments": ["Agreed!", "Sometimes my poetry doesn't compile though."]
    },
    {
        "id": 3,
        "username": "chef_marina",
        "content": "Perfected my sourdough starter recipe today. Look at that crust! 🥖",
        "timestamp": "1 hour ago",
        "likes": 310,
        "comments": ["Drop the recipe please!", "Looks delicious!"]
    }
]

# --- CORE FUNCTIONS ---

def display_feed(feed):
    """Prints the social media feed to the console."""
    print("\n" + "="*40)
    print("         📱 MY SOCIAL FEED 📱         ")
    print("="*40 + "\n")
    
    for post in feed:
        print(f"@{post['username']} • {post['timestamp']}")
        print(f"👉 {post['content']}")
        print(f"❤️ {post['likes']} Likes  |  💬 {len(post['comments'])} Comments")
        if post['comments']:
            print(f"   Recent comment: \"{post['comments'][-1]}\"")
        print("-" * 40)

def like_post(feed, post_id):
    """Finds a post by ID and increments its like count."""
    for post in feed:
        if post['id'] == post_id:
            post['likes'] += 1
            print(f"\n✅ You liked @{post['username']}'s post!")
            return
    print("\n❌ Post not found.")

def add_comment(feed, post_id, comment_text):
    """Finds a post by ID and appends a new comment."""
    for post in feed:
        if post['id'] == post_id:
            post['comments'].append(comment_text)
            print(f"\n✅ Comment added to @{post['username']}'s post!")
            return
    print("\n❌ Post not found.")

# --- SIMULATION RUNNER ---

def main():
    # 1. Display the initial feed
    display_feed(DUMMY_FEED)
    time.sleep(1)
    
    # 2. Simulate user interaction: Liking a post
    print("\n[Action] Simulating user liking Post #1...")
    like_post(DUMMY_FEED, post_id=1)
    time.sleep(1)
    
    # 3. Simulate user interaction: Adding a comment
    print("\n[Action] Simulating user commenting on Post #2...")
    add_comment(DUMMY_FEED, post_id=2, comment_text="Beautifully said.")
    time.sleep(1)
    
    # 4. Display the updated feed
    print("\n--- Fetching updated feed... ---")
    time.sleep(1)
    display_feed(DUMMY_FEED)

if __name__ == "__main__":
    main()
