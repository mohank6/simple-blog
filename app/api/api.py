# Invalid input
INVALID_INPUT = 100
TOO_MANY_REQUEST = 101

# Author
INVALID_LOGIN_TOKEN = 300
UNAUTHORIZED = 301
AUTHOR_NOT_FOUND = 302
INVALID_PASSWORD = 303
ADMIN_USER_NOT_FOUND = 304

# Post
POST_NOT_FOUND = 400

# Category
CATEGORY_NOT_FOUND = 401

# Comment
COMMENT_NOT_FOUND = 402


error_messages = {
    INVALID_INPUT: 'Invalid input',
    TOO_MANY_REQUEST: 'Too many requests',
    INVALID_LOGIN_TOKEN: 'Invalid token for login',
    UNAUTHORIZED: "Unauthorized",
    AUTHOR_NOT_FOUND: "Author not found",
    INVALID_PASSWORD: "Invalid password",
    POST_NOT_FOUND: "Post not found",
    CATEGORY_NOT_FOUND: "Category not found",
    COMMENT_NOT_FOUND: "Comment not found",
    ADMIN_USER_NOT_FOUND: "Admin user not found",
}
