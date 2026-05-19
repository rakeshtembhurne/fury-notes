---
created: 2024-01-15
tags: [tech, programming, nodejs, backend]
---

# NodeJS Reference Notes

## Core Concepts
- Non-blocking, event-driven
- Built on V8 engine
- Single-threaded, async I/O
- NPM for package management

## Modules
- **Core Modules**: fs, http, path, os, events, util, url
- **Local Modules**: Custom modules with require/export
- **Third-party**: Express, lodash, mongoose (via npm install)

## Event Loop
- Call Stack (LIFO) + Callback Queue (FIFO)
- Phases: Timers → I/O callbacks → Poll → Check → Close callbacks
- Microtasks (process.nextTick, Promises) run between phases
- Macrotasks (setTimeout, setImmediate) run in next iteration

## Key APIs
- **Streams**: Readable, Writable, Duplex, Transform
- **File System**: readFile, writeFile, mkdir, rmdir
- **HTTP**: http.createServer(), req, res
- **Events**: EventEmitter, on(), emit()
- **Child Process**: spawn, exec, fork

## Express.js
- Middleware (app.use)
- Routing (app.get, app.post, etc.)
- Static files (express.static)
- Template engines (EJS, Pug)

## MongoDB/Mongoose
- Schema, Model, Document
- CRUD operations
- Query, Aggregation, Indexes

## Authentication
- JWT, OAuth, Passport
- Cookie, Session
- Bcrypt for hashing

## Deployment
- PM2, Nginx
- AWS, Heroku, Docker
- Redis/Memcached for caching
