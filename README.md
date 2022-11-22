# PythonicBrain

### Install

```bash
pip install PythonicBrain
```


## Available functions

```python
from PythonicBrain.PBTable import table
- table(): prints a data table provided as list

table([[1,2,3,4],[3,4,5,6]])

```

```python
from PythonicBrain.PBDecorators import executiontime

- @executiontime [decorator] : prints the time of execution of a parameter

@executiontime
def hello()
    --

```
```python
from PythonicBrain.PBInteger import *

- float_range() : Returns a iterable of floating range

float_range(start, stop, step)


```
```python
from PythonicBrain.PBString import *

- random_string() : return a random string of given length and character set

print(random_string(54))


- slugify() : Returns a slug text from given vlaue

slugify(hello world)


- splash() : return a string with given splash style

splash(hello world)


- headline() : return a formatted string in headline style

headline(hello world)

- multiline_input() : takes multiline user input

 inp=multiline_input()
 print(inp)



```



