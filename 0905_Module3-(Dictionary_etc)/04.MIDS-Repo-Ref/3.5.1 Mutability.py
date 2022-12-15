###### More about Mutability

# The ability to change the contents of a list is a large part of why this is
# such a powerful type.   Mutability becomes especially important when objects
# get large.  Imagine that you had a large list with millions of items - it
# would be rather inefficient if you had to create an entirely new list every
# time you changed one entry.

# At the same time, mutable objects present a set of challenges, and it can be
# easy to make mistakes as a programmer.  The following code demonstrates this.

# Notice that we create two variables, first_list and second_list.  Once we have
# two list variables, we might want to use each one for a different purpose.
# Here we try to make the first value in second_list equal to 1000.  Finally, we
# print the value of first_list

# # Demonstrates that mutable objects can have multiple names
# first_list = [1,2,3,4,5]
# second_list = first_list
# second_list[0] = 1000
# print("first_list now has the value",first_list)

# Notice that the original list has changed as well!  That's because we created
# two variables, but they both point to the same list object.  It doesn't matter
# which variable we use to change the object, the end result is the same.

# This is one advantage of immutable data structures - they prevent you from
# making this kind of mistake because you can't modify things that have already
# been created.

# It may seem surprising that creating a new variable doesn't create a second
# list object, but remember that objects can get very large in memory.  It would
# be rather wasteful if the Python interpreter copied them by default every time
# there was a variable assignment.  As you'll see, it's very common to have
# multiple variables point to the same object, but pretty rare that you actually
# want to make a copy of the object.

# Now try to predict what the following code snippet will output.

# # Demonstrates mutating nested lists
# a_list = ["tu", "tu"]
# b_list = [a_list]
# c_list = [a_list]
# b_list[0][1] = "ba"
# print("c_list now has the value", c_list)


# To understand what's happening, it may help to draw a picture. Both b_list and
# c_list are lists that contain a_list as their one item.  When you change
# a_list through b_list, the contents of c_list change as well.

# Here are two more snippets for you to think about.

# # Demonstrates more mutating of nested lists
# a_list = []
# b_list = ["ra", a_list]
# c_list = [a_list, a_list]
# b_list[1].append("ta")
# print(b_list, c_list)


# # Demonstrates a circular list reference
# a_list = ["go"]
# a_list.append(a_list)
# print(a_list)


# The last snippet is especially surprising.  In Python, you're allowed to place
# a list inside of itself - list references can be circular. Of course, there's
# no way to print the list when you do this.  This may be clear if you draw a
# picture of the references.  a_list contains "go", then a list that contains
# "go" and whose second element is a list that contains "go" and whose second
# element is a list... It would take an infinite amount of space to print this
# list, so Python represents the circularity using '...'.

# ## Copies and Deep Copies

# While not as common as you might expect, there are times when you need to make
# a copy of a list object.  There is a `copy()` method that does this for you.
# However, this may not be as straightforward as you expect.

# # Demonstration of copy method.
# a_list = [1, 2, ["Bill", "Kay"]]
# b_list = a_list.copy()
# print("b_list now has the value", b_list)
#
# a_list[0] = 5
# print("a_list now has the value", a_list)
# print("b_list now has the value", b_list)


# Now it looks like we successfully created two separate lists, and even changed
# one of them so that their contents are different.  Does this mean that b_list
# will be unchanged no matter what we do to a_list?  Consider the following
# code.

# # Demonstrates that a_list and b_list share items
# a_list = [1, 2, ["Bill", "Kay"]]
# b_list = a_list.copy()
# a_list[2].append("Paul")
# print("b_list now has the value", b_list)


# b_list is now different as well.  That's because the `copy` method only makes
# a `shallow copy` of a_list.  It creates a new list object in object space, but
# all of its references just point to the same place that the original list's
# references pointed to.  So the inner list that was contained inside a_list
# doesn't get copied.  In the end, a_list and b_list are separate list objects,
# but both contain the same list as an item.

# If we want to make a `deep copy` of the list, what should we do?  Python has a
# deepcopy method that will try to replicate an object, including all the
# objects that can be reached by reference from it.

# # Demonstrates use of deepcopy
# from copy import deepcopy
# a_list = [1, 2, ["Bill", "Kay"]]
# c_list = deepcopy(a_list)
# a_list[2].append("Did I get it?")
# print(a_list)
# print(c_list)


# In order to make a deep copy, we have to create a copy of all list items, then
# all items contained in those items, and so forth. Now this isn't something
# that is going to come up every day but it's a great thing to be aware of
# because you will come across it at some point.

# Just a little warning: a deep copy will work its way through every object that
# can be reached through list references - and that could be a lot of objects.
# If you're not careful, you could be waiting for a huge amount of data to be
# replicated - use this method with caution.

# We've seen a lot of detailed features of the way lists work.  As a key take
# away, remember that variables are not objects themselves, they point to
# objects.  Similarly, lists point to the objects they contain.  When you change
# an object, think about all the variables and lists that point to that object -
# they are all affected.
