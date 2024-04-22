# format_spec     ::=  [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"



x = 22

# Print an empty line for spacing.
print()

# Print the original value of 'x' with a label.
print("Original Number: ", x)

# Format and print the value of 'x' with left alignment, a width of 10 characters, and padding using spaces.
print("Left aligned (width 10)   :" + "{:< 10d}".format(x))

# Format and print the value of 'x' with right alignment, a width of 10 characters, and padding using spaces.
print("Right aligned (width 10)  :" + "{:10d}".format(x))

# Format and print the value of 'x' with center alignment, a width of 10 characters, and padding using spaces.
print("Center aligned (width 10) :" + "{:^10d}".format(x))

# Print an empty line for spacing.
print()
