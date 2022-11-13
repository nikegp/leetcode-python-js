## Solving LeetCode challenges for fun.
Before executing a given solution start the project   
```
docker-compose up
```

To validate/execute a given solution

```
./run-challenge.sh python 1544
./run-challenge.sh js 1544
```

The ID can be anything, and it's a folder with the solution, although I use LeetCode challenge id here.

### Tech stack
Python 3.10, Javascript/TypeScript.
Python is formatted with Black, JS with Prettier.

### Package management

For JS solutions (Node.js container)
```
./install.sh js install mongo
./install.sh js remove mongo
```

### LeetCode compatibility
All the solutions are written to match the signatures in the original LeetCode challenges whenever possible, so they can be
copy/pasted there. As a side effect, sometimes camelCase and snake_case are mixed only to keep the compatibility.
As for the JS solutions, I write them with TypeScript that isn't currently supported by LeetCode so the solutions
require a minor edit before pasting there.
