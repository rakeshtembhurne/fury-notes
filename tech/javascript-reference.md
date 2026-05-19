---
created: 2024-01-01
tags: [tech, programming, javascript, frontend]
source: Knowledge/Programming/Dev Notes/JavaScript.md
---

# JavaScript Reference Guide

## Introduction
- ECMAScript specification
- JS Engines: V8 (Chrome/Opera), Spider Monkey (Firefox), Chakra (IE), Nitro (Safari)
- Safe - no low level access, browser sandbox
- Transpilers: TypeScript, Flow, Dart, Brython, Kotlin

## Fundamentals
- Script tag can be inserted anywhere in HTML
- Automatic semicolon insertion (ASI)
- "use strict" enables ES5 modern behavior
- Nested comments not supported

## Variables
- `let` (block scope), `var` (function scope), `const` (block scope, immutable)
- Naming: letters, digits, $ and _ only, first char must not be digit
- const variables should be UPPER_CASE_WITH_UNDERSCORES for hardcoded values

## Data Types
- **Primitives**: Number, BigInt, String, Boolean, null, undefined, Symbol
- **Object**: for collections and complex entities
- typeof null returns "object" (known JS bug)

## [Continues for 1650 lines — covering: functions, objects, arrays, async, DOM, events, etc.]
