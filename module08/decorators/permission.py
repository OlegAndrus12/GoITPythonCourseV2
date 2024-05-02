def authorize(user_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_type == "admin":
                return func(*args, **kwargs)
            else:
                raise PermissionError("You are not authorized to access this function.")

        return wrapper

    return decorator


@authorize(user_type="moderator")
def admin_function():
    return "Admin access granted."


print(admin_function())
