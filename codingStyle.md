---
title: Coding Style
lastEdited: 2017-04-12
---

# Coding Style

I'll follow project styles but these are some of my preferences.

```java
if (someVar) {

}
```

In general I defer formatting to my editor's formatter. 

In absence of a language naming convention, I'll use camelCase.

Google's style guides are a good reference but I can still dissagree.

### java

`final` does not mean all caps. [Google](https://google.github.io/styleguide/javaguide.html#s5.2.4-constant-names) understands.

### python

Python is super useful. Its great. But the style makes me sad. Significant white space is bad. I'm not the biggest fan of truthy values other than booleans. So I don't really use them and I go against [google](https://google.github.io/styleguide/pyguide.html?showone=True/False_evaluations#True/False_evaluations). No point in remembering the differences of javascript, python, and others in how things are evaluated.

### javascript

Use `const` and `let` instead of `var`. Also use typescript.

