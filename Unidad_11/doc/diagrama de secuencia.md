This is a mermaid diagram, you may need to install a [Browser Plugin](https://github.com/BackMarket/github-mermaid-extension) or [VsCode extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) or similar to view it.

You can also [view it full screen as an SVG](https://mermaid.ink/svg/c2VxdWVuY2VEaWFncmFtCiAgc3RhcnQtPj5hZGQ6IGNhbGxzIHgzCiAgYWRkLS0+PnN0YXJ0OiByZXR1cm5zIGZsb2F0CiAgc3RhcnQtPj5zdWJ0cmFjdDogY2FsbHMgeDMKICBzdWJ0cmFjdC0tPj5zdGFydDogcmV0dXJucyBmbG9hdAogIHN0YXJ0LT4+bXVsdGlwbHk6IGNhbGxzIHgzCiAgbXVsdGlwbHktLT4+c3RhcnQ6IHJldHVybnMgZmxvYXQKICBzdGFydC0+PmRpdmlkZTogY2FsbHMgeDQKICBkaXZpZGUtLT4+c3RhcnQ6IHJldHVybnMgZmxvYXQK)        

```mermaid
sequenceDiagram
  start->>add: calls x3
  add-->>start: returns float
  start->>subtract: calls x3
  subtract-->>start: returns float
  start->>multiply: calls x3
  multiply-->>start: returns float
  start->>divide: calls x4
  divide-->>start: returns float

```
