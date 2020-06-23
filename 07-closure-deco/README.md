# Notes

* Decorator:
  * A function that takes another function
  * Extends the behavior of that function
  * Without explicitly modifying that function
  * Really just a syntactic sugar
  * Executed as soon as the module is imported

* Closure:
  * A function that retains the bindings of the free variables that exist when the function is defined, so that they can be used later when the function is invoked and the defining scope is no longer available.
  * The only situation in which a function may need to deal with external variables that are nonglobal is when it is nested in another function.
  * We have closures when:
    * We have a nested function (function inside a function).
    * The nested function refers to a variable defined in the enclosing function.
    * The enclosing function returns the nested function.
  * Use it to avoid use of global variables and as a light weight version of a class.
