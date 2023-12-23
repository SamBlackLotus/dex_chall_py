# Questions and Answers

Q. Should I add typing to ALL variables?
> A. No, in general we should add typings on functions arguments and returns, we only add typing on variables if you use the same variable for multiple purposes, and for external libraries that it's not obvious the return type.

Q. Do I need to add docstrings about all the variables?
> A. No, you need to describe the function overall functionality, the arguments, returns and possible exceptions.

Q. Should I create typeddict for all the returns?
> A. No, only for the core logs, e.g. battle results.

Q. What is Union type?
> A. It's used to describe multiple types possibilities, for example, if you will return a string or a integer from a function.

Q. How does it work the type Dict?
> A. Dict type receives 2 arguments, one to describe the key and another for the values, so for example if you have homogenous values you would describe mode than one type in the second arguments, e.g. Dict[str, Union[str, int]].