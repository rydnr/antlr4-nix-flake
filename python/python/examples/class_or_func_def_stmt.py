# vim: set fileencoding=utf-8
# class_or_func_def_stmt: decorator+ (classdef | funcdef);

# decorator classdef
@decorator
class foo:
    pass

# decorator decorator funcdef
@accepts(int,int)
@returns(float)
def bar(low,high):
    pass
