IOET challenge interview
=======

There's a function to call to make automatically

### run this snipet if you make the files to test the script

```python
file_content ="""
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
"""
def make_files_content() -> None:
    with open("<file_name.txt>", "w") as f:
        f.write(file_content)
```

or only run:
```
python main.py
```


### In this part the best decission is use the power of the regular expressions

```python
schedule = dict()
    
for x in file:
    name = re.search(r'\w{4,}', x)
    content = re.findall(r'\=(.*)', x)
    schedule[name.group()] = content[0].split(",")


name : RENE
content : ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']

name : ASTRID
content : ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']

name : ANDRES
content : ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']

```


### But to make more Pythonist the process, i used a dictionary comprehension like this.
```python
schedule = {re.search(r'\w{3,}', x).group():re.findall(r'\=(.*)', x)[0].split(",") for x in file }
```


### This is the main procedure, an iterative loop for each key value
### and comparate with the other iteration over the same dictionary
### then i call the function match_keys

```python
try:
    for key,value in schedule.items():
        for new_key, new_value in schedule.items():
            if key != new_key:
                print(f"{key}-{new_key}:{match_keys(value, new_value)}")
            else:
                break
except Exception as e:
    print(str(e))
```


### function *_match_keys_*
### take the values of two arrays and check 
### analyze the coincidences in the scheduling arrays
```python
def match_keys(value_1: List[str], value_2: List[str]) -> int:
    
    schedule_match = [value for value in value_1 if value in value_2]
    return len(schedule_match)
```


### This is the output:
<img src=".github/output.png"/>