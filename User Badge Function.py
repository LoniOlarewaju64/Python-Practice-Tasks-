def create_user_badge(username, access_level="Standard"):
   
    # Constructing the unified multi-line string
    
    badge = f"USER BADGE: {username} ACCESS LEVEL: {access_level}"
    return badge

print(create_user_badge("loni o."))

print("-" * 20) # Just a visual separator

# Print with a custom access level
print(create_user_badge("lonit", "Admin"))


# Example usage:
# print(create_user_badge("Alice"))
# print(create_user_badge("Bob", "Admin"))