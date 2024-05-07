# conditionals
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# short circuiting
# to check if both are True use and while or only looks for one True
is_Friend = False
is_user = True


if is_friend or is_user:
  print("we friends forever!")
