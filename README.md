## Python Top Formatter

Python script to output the result of the Linux top command to a file of desired type in the current directory.

Supported formats:
- "txt"
- "csv"
- "json" (WIP)

Any other file extension is invalid. Improvements in progress for additional file types and better formatting.

### Usage

```
from top_formatter import top_formatter

output = top_formatter("txt")
```

### WIP

#### json

- Issue with the json output where values seperated with a space are being added to a seperate column. Will need to amend the regex.