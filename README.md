### Solving LeetCode challenges for fun.
Before executing a given solution start the project   
```
docker-compose up
```

To validate/execute a given solution

```
./run-challenge.sh python 1544
./run-challenge.sh js 1544
```

The ID can be anything, although I use LeetCode challenge id here.

### Tech stack
Python 3.10, Javascript/TypeScript.
Python is formatted with Black, JS with Prettier.

### Package management

For JS solutions (Node.js container)
```
./install.sh js install mongo
./install.sh js remove mongo
```


