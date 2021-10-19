IOET challenge interview
=======



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


### This is the output.
<img src=".github/schedule.png" />