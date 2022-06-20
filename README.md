```mermaid
flowchart LR
  subgraph bg [Notebook Overview]
    direction LR
    studying(((Studying))) --> learning(((Learning))) --> writing(((Writing)))
    click studying "./studying/readme.md" _self
    click learning "learning/readme.md" "Learning"
    click writing "./writing/readme.md" "Writing"
  end
  style bg fill:#6c757d
```

```mermaid
flowchart LR
  subgraph bg [三大基本能力]
    direction LR
    brains(((脑力\n独立思考))) --> self-discipline(((自律\n忍耐克制)))
    self-discipline(((自律\n忍耐克制))) --> loneliness(((寂寞\n读书学习)))
    loneliness(((寂寞\n读书学习))) --> brains(((脑力\n独立思考)))
  end
  style bg fill:#6c757d
```
